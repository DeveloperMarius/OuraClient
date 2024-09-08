from bleak import BleakScanner
from Crypto.Cipher import AES
from oura import OuraClient
import asyncio


async def main():
    # authkey: 2410324e29504887dc73f2de912fa2274588
    async with OuraClient("A0:38:F8:37:5E:00") as client:

        try:
            auth_key = bytes.fromhex("deadbeefcafeaffeabadbabe11111111")
            response = await client.raw_request(bytes([47, 16, *auth_key]))
            print('Auth response: ' + response.hex())
        except Exception as e:
            print('Auth Error')


asyncio.run(main())
