from oura import OuraClient
from oura.exceptions.missing_response_error import MissingResponseError
import asyncio

async def main():
    async with OuraClient("A0:38:F8:37:5E:00") as client:
        for i in range(0x0, 63):
            if i in [26]:
                continue
            print(f'Attempting Operation {i}')
            try:
                response = await client.raw_request(bytes([i, 0x0]))
                print(f'Response: {response}')
            except MissingResponseError as e:
                print(f'MissingResponseError: {e}')
            except Exception as e:
                print(f'Error: {e}')

asyncio.run(main())

# Not found error: bytearray(b'0\x01\xf1')
# Fehler = Missing Response
# v = await client.raw_request(bytes([47, 0x0]))
# print(v)
    # auth_key = bytes.fromhex("324e29504887dc73f2de912fa2274588")
# Connecting...
# Connected
# Paired: True
# Attempting Operation 0
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 1
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 2
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 3
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 4
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 5
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 6
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 7
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 8
# Response: bytearray(b'\t\x12\x01\x12\x00\x02\n\x04\x01\x00\x01\x05\x00\x0c\x1c^7\xf88\xa0')
# Attempting Operation 9
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 10
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 11
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 12
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 13
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 14
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 15
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 16
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 17
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 18
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 19
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 20
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 21
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 22
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 23
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 24
# Response: bytearray(b'\x19\x01\x01')
# Attempting Operation 25
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 27
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 28
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 29
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 30
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 31
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 32
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 33
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 34
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 35
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 36
# MissingResponseError:
# Attempting Operation 37
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 38
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 39
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 40
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 41
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 42
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 43
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 44
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 45
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 46
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 47
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 48
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 49
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 50
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 51
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 52
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 53
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 54
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 55
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 56
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 57
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 58
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 59
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 60
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 61
# Response: bytearray(b'/\x02/\x01')
# Attempting Operation 62
# Response: bytearray(b'/\x02/\x01')
