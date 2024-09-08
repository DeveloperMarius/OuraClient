from bleak import BleakScanner
from Crypto.Cipher import AES
from oura import OuraClient
import asyncio


async def main():
    auth_key = bytes.fromhex('324e29504887dc73f2de912fa2274588')
    async with OuraClient("A0:38:F8:37:5E:00") as client:
        client.get_data()


asyncio.run(main())
