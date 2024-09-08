import asyncio
from asyncio import CancelledError
from bleak import BleakClient, BleakError
from Crypto.Cipher import AES
import os
import time
from oura.exceptions import AuthenticationError, InFactoryResestError, NotOriginalOnboardedDeviceError, MissingResponseError, InvalidResponseTagError
from oura.models import BatteryInfo, VersionInfo, EventPacket


class OuraClient:
    _SERVICE_UUID = "98ed0001-a541-11e4-b6a0-0002a5d5c51b"
    _WRITE_CHARACTERISTIC_UUID = "98ed0002-a541-11e4-b6a0-0002a5d5c51b"
    _READ_CHARACTERISTIC_UUID = "98ed0003-a541-11e4-b6a0-0002a5d5c51b"
    
    
    def __init__(self, mac_addr: str, authentication_secret: bytes = None):
        self._authenticated = False
        self._authentication_secret = authentication_secret
        self._client = BleakClient(mac_addr, services=[OuraClient._SERVICE_UUID, '00001800-0000-1000-8000-00805f9b34fb', '00060000-f8ce-11e4-abf4-0002a5d5c51b', '00001801-0000-1000-8000-00805f9b34fb'])
        self._read_queue = asyncio.Queue()

    def notification_handler(self, _sender, data):
        self._read_queue.put_nowait(data)

    async def connect(self):
        print('Connecting...')
        await self._client.connect(timeout=15)
        print('Connected')
        # Paring seems to be required on Windows to read characteristics
        if os.name == 'nt':
            paired = await self._client.pair()
            print(f"Paired: {paired}")
        await self._client.start_notify(OuraClient._READ_CHARACTERISTIC_UUID, self.notification_handler)
        if self._authentication_secret is not None:
            await self.authenticate(self._authentication_secret)

    async def __aenter__(self):
        await self.connect()
        return self
    
    async def disconnect(self):
        await self._client.disconnect()
        return True

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()

    @property
    def client(self):
        return self._client

    async def raw_request(self, data:bytes, until:callable = None, timeout=15) -> bytes|list[bytes]:
        if not self.client.is_connected:
            raise BleakError('Not connected')
        await self.client.write_gatt_char(OuraClient._WRITE_CHARACTERISTIC_UUID, bytes(data))

        if until is None:
            try:
                response = await asyncio.wait_for(self._read_queue.get(), timeout=timeout)
            except TimeoutError:
                raise MissingResponseError()
            except CancelledError:
                raise MissingResponseError()
            return response
        else:
            data: list[bytes] = []
            end_time = int(time.time()) + timeout
            while (len(data) == 0 or not until(data[-1])) and int(time.time()) < end_time:
                print(f'Time left: {end_time - time.time()} secs')
                try:
                    data.append(await asyncio.wait_for(self._read_queue.get(), timeout=(end_time - time.time())))
                    print(data[-1])
                except TimeoutError:
                    break
                except CancelledError:
                    break
            if len(data) == 0:
                raise MissingResponseError()
            return data

    async def get_version_info(self) -> VersionInfo:
        # No Auth Required
        raw_response = await self.raw_request(bytes([8, 3, 0, 0, 0]))
        return VersionInfo.from_bytes(raw_response)

    async def get_battery_level(self) -> BatteryInfo:
        if not self._authenticated:
            raise AuthenticationError()
        raw_response = await self.raw_request(bytes([12, 0]))
        return BatteryInfo.from_bytes(raw_response)

    async def get_capabilities(self, page=0):
        raw_response = await self.raw_request(bytes([47, 2, 1, page]))
        # page 0: 2f12020200050102020303020401050107000800
        # page 1: 2f0c020209000a060b000c000d00
        # page 2: 2f020202 <- no data returned
        return raw_response

    async def set_ble_mode(self):
        pass

    async def check_sleep_analysis(self):
        raw_response = await self.raw_request(bytes([40, 1, 0]))
        return raw_response

    async def enable_bundling(self):
        raw_response = await self.raw_request(bytes([47, 2, 3, 1]))
        return raw_response

    async def set_manufacturing_info(self, modus: int):
        # Operation: SetManufacturingInfo
        # TEST=0x0, PROD=0x1
        request_data = bytes([55, 5, 1, 7, 0, 0, 0]) if modus == 1 else bytes([55, 5, 1, 3, 0, 0, 0])
        raw_response = await self.raw_request(request_data)
        return raw_response


    async def get_event(self, start_timestamp=0, max_events=255) -> EventPacket:
        start_timestamp_bytes: bytes = start_timestamp.to_bytes(4, 'big')
        start_timestamp_ints = list(start_timestamp_bytes)
        def until(data:bytes) -> bool:
            # Multiple EventSummary's are return and the events will not always end with one
            #for i in range(0, len(data), 20):
            #    if data[i] == 17:
            #        return True
            return False
        raw_response = await self.raw_request(bytes([16, 9, *start_timestamp_ints, min(255, max_events), 0xff, 0xff, 0xff, 0xff]), until=until)
        events = []
        for packet in raw_response:
            event_packet = EventPacket.from_bytes(packet)
            events += event_packet.events
        return EventPacket(events)

    async def get_data(self):
        enable_bundling_response = await self.enable_bundling()
        print(enable_bundling_response)
        #check_sleep_analysis_response = await self.check_sleep_analysis()
        #print(check_sleep_analysis_response)
        data = await self.get_event()
        print(data)
        print(len(data.events))

    async def reset_memory(self):
        # In an Android HCI Log the reset response was sent after 76 secs
        raw_response = await self.raw_request(bytes([26, 0]), timeout=150)
        if raw_response[2] != 0:
            raise Exception('Failed to reset memory')
        await self._client.unpair()
        return raw_response

    async def set_auth_key(self, key: bytes) -> bool:
        assert len(key) == 16, "Key must be 16 bytes long"
        raw_response = await self.raw_request(bytes([36, 16, *key]))
        print(raw_response.hex())
        # assert raw_response[0] == 37, "Invalid response tag"
        # assert raw_response[2] in [0, 5], "Invalid response code"
        return raw_response[2] == 0

    async def auth_nonce(self):
        raw_nonce_response = await self.raw_request(bytes([47, 1, 43]))
        # 15 Byte Nonce!
        auth_nonce = raw_nonce_response[3:18]
        print("Received nonce:", auth_nonce.hex())
        return auth_nonce

    async def authenticate(self, secret, nonce=None):
        # First, get the challenge from the ring
        raw_nonce = await self.auth_nonce() if nonce is None else nonce
        auth_nonce = raw_nonce + bytes([1])

        # Encrypt the challenge
        cipher = AES.new(secret, AES.MODE_ECB)
        encrypted = cipher.encrypt(auth_nonce)

        response = await self.raw_request(bytes([47, 17, 45, *encrypted]))

        if response[3] == 0x0:
            self._authenticated = True
            print("Authenticated with ring!")
        elif response[3] == 0x1:
            raise AuthenticationError()
        elif response[3] == 0x2:
            raise InFactoryResestError()
        elif response[3] == 0x3:
            raise NotOriginalOnboardedDeviceError()
        else:
            raise InvalidResponseTagError()