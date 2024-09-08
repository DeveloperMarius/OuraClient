from bleak import BleakClient
import asyncio

async def main():
    _read_queue = asyncio.Queue()
    services = ['00001800-0000-1000-8000-00805f9b34fb']

    def notification_handler(_sender, data):
        _read_queue.put_nowait(data)

    async with BleakClient("A0:38:F8:37:5E:00", services=services) as client:
        await client.pair()
        await client.start_notify("98ed0003-a541-11e4-b6a0-0002a5d5c51b", notification_handler)
        await client.write_gatt_char("98ed0002-a541-11e4-b6a0-0002a5d5c51b", bytes([8, 3, 0, 0, 0]))
        response = await asyncio.wait_for(_read_queue.get(), timeout=15)
        print(f"Version Information: {response.hex()}")
        await client.unpair()


if __name__ == '__main__':
    asyncio.run(main())