from bleak import BleakScanner
from Crypto.Cipher import AES
from oura import OuraClient
import asyncio

async def main():
    # authkey: 2410324e29504887dc73f2de912fa2274588
    async with OuraClient("A0:38:F8:37:5E:00") as client:

        #response = await client.raw_request(bytes([0x1a, 0x00]))
        #print(response.hex())
        nonce1 = await client.auth_nonce()

        auth_key = bytes.fromhex("324e29504887dc73f2de912fa2274588")
        cipher = AES.new(auth_key, AES.MODE_ECB)
        encrypted = bytes.fromhex("324e29504887dc73f2de912fa2271111")
        try:
            response = await client.raw_request(bytes([47, 17, 45, *encrypted]))
            print('Auth response: ' + response.hex())
        except Exception as e:
            print('Auth Error')
        encrypted = bytes.fromhex("324e29504887dc73f2de912fa2272222")
        try:
            response = await client.raw_request(bytes([47, 17, 45, *encrypted]))
            print('Auth response: ' + response.hex())
        except Exception as e:
            print('Auth Error')

        #nonce3 = await client.auth_nonce()
        nonce2 = await client.auth_nonce()
        print('Connected?: ')
        print(client.client.is_connected)

        encrypted = bytes.fromhex("324e29504887dc73f2de912fa2273333")
        try:
            response = await client.raw_request(bytes([47, 17, 45, *encrypted]))
            print('Auth response: ' + response.hex())
        except Exception as e:
            print('Auth Error')

        print('Connected?: ')
        print(client.client.is_connected)
        encrypted = bytes.fromhex("324e29504887dc73f2de912fa2274444")
        try:
            response = await client.raw_request(bytes([47, 17, 45, *encrypted]))
            print('Auth response: ' + response.hex())
        except Exception as e:
            print('Auth Error')
        print('Connected?: ')
        print(client.client.is_connected)

        encrypted = cipher.encrypt(nonce2 + bytes([1]))
        try:
            response = await client.raw_request(bytes([47, 17, 45, *encrypted]))
            print('Auth response: ' + response.hex())
        except Exception as e:
            print('Auth Error')

        print(await client.get_battery_level())

        print("Authenticated with ring!")
asyncio.run(main())
