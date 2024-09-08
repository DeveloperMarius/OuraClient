from oura import OuraClient
import asyncio
import sys
import subprocess
import time

async def main():
    failed = 0
    requests = 0
    times = []
    while True:
        try:
            start = time.time()
            async with OuraClient("A0:38:F8:37:5E:00") as client:
                paired = await client.client.pair()
                print(f"Paired: {paired}")
                with open('nonces.json', 'a') as file:
                    nonce = await client.auth_nonce()
                    file.write(f'"{nonce.hex()}",')
                    nonce = await client.auth_nonce()
                    file.write(f'"{nonce.hex()}",')
                failed = 0
                requests += 1
            end = time.time()
            times.append(end - start)
        except Exception as e:
            print(e)
            failed += 1
            if failed > 3:
                break
            print(f'Failed to connect #{failed}')
            await asyncio.sleep(3)
    if len(times) > 0:
        print(f'\nAverage request time: {sum(times) / len(times)}')
    print(f'\nFailed to connect after {requests} requests')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        while True:
            print('\n\nStarting fetch instance...')
            process = subprocess.Popen(['python', 'demo.py', 'fetch'])
            process.wait()
    if len(sys.argv) > 1 and sys.argv[1] == 'fetch':
        asyncio.run(main())
