from oura import OuraClient
import asyncio

async def main():
    # auth_key = bytes.fromhex("324e29504887dc73f2de912fa2274588")
    new_key = bytes.fromhex("324e29504887dc73f2de912fa2274522")
    async with OuraClient("A0:38:F8:37:5E:00") as client:
        v = await client.get_version_info()
        print(v)
        await client.reset_memory()
    async with OuraClient("A0:38:F8:37:5E:00") as client:
        print('Setting')
        await client.set_auth_key(new_key)
        print('Authenticating')
        await client.authenticate(new_key)
        print('Getting data')
        await client.get_data()
   # async with OuraClient("A0:38:F8:37:5E:00") as client:
   #     paired = await client.client.pair()
   #     print(f"Paired: {paired}")
   #     await client.authenticate(new_key)
   #     await client.get_data()



asyncio.run(main())
