from oura import OuraClient
from oura.exceptions.missing_response_error import MissingResponseError
import asyncio

async def main():
    auth_key = bytes.fromhex("324e29504887dc73f2de912fa2274522")
    async with OuraClient("A0:38:F8:37:5E:00", auth_key) as client:
        for i in range(0x0, 0x100):
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
# Received nonce: 8c2e7c0adda030865dc5201ddfbb0f
# Authenticated with ring!
# Attempting 0
# MissingResponseError:
# Attempting 1
# MissingResponseError:
# Attempting 2
# MissingResponseError:
# Attempting 3
# MissingResponseError:
# Attempting 4
# MissingResponseError:
# Attempting 5
# MissingResponseError:
# Attempting 6
# bytearray(b'\x07\x01\x01')
# Attempting 7
# MissingResponseError:
# Attempting 8
# bytearray(b'\t\x12\x01\x12\x00\x02\n\x04\x01\x00\x01\x05\x00\x0c\x1c^7\xf88\xa0')
# Attempting 9
# MissingResponseError:
# Attempting 10
# bytearray(b'\x0b\n\x00\x00\x00\x00\xff\xff\xff\xff01')
# Attempting 11
# MissingResponseError:
# Attempting 12
# bytearray(b'\r\x06cc\x00\x00M\x10')
# Attempting 13
# MissingResponseError:
# Attempting 14
# bytearray(b'\x0f\x01\x00')
# Attempting 15
# MissingResponseError:
# Attempting 16
# MissingResponseError:
# Attempting 17
# MissingResponseError:
# Attempting 18
# MissingResponseError:
# Attempting 19
# MissingResponseError:
# Attempting 20
# MissingResponseError:
# Attempting 21
# MissingResponseError:
# Attempting 22
# MissingResponseError:
# Attempting 23
# MissingResponseError:
# Attempting 24
# bytearray(b'\x19\x01\x01')
# Attempting 25
# MissingResponseError:
# Attempting 26
# MissingResponseError:
# Attempting 27
# MissingResponseError:
# Attempting 28
# bytearray(b'\x1d\x01\x01')
# Attempting 29
# MissingResponseError:
# Attempting 30
# MissingResponseError:
# Attempting 31
# MissingResponseError:
# Attempting 32
# MissingResponseError:
# Attempting 33
# MissingResponseError:
# Attempting 34
# bytearray(b'#\x02\xff\xff')
# Attempting 35
# MissingResponseError:
# Attempting 36
# MissingResponseError:
# Attempting 37
# MissingResponseError:
# Attempting 38
# bytearray(b"\'\x01\x00")
# Attempting 39
# MissingResponseError:
# Attempting 40
# bytearray(b')\x01\x00')
# Attempting 41
# MissingResponseError:
# Attempting 42
# MissingResponseError:
# Attempting 43
# MissingResponseError:
# Attempting 44
# MissingResponseError:
# Attempting 45
# MissingResponseError:
# Attempting 46
# MissingResponseError:
# Attempting 47
# MissingResponseError:
# Attempting 48
# MissingResponseError:
# Attempting 49
# bytearray(b'2\x04\x00\x00\x00\x00')
# Attempting 50
# MissingResponseError:
# Attempting 51
# MissingResponseError:
# Attempting 52
# MissingResponseError:
# Attempting 53
# MissingResponseError:
# Attempting 54
# MissingResponseError:
# Attempting 55
# bytearray(b'8\x01\x01')
# Attempting 56
# MissingResponseError:
# Attempting 57
# bytearray(b':\x01\x00')
# Attempting 58
# MissingResponseError:
# Attempting 59
# MissingResponseError:
# Attempting 60
# MissingResponseError:
# Attempting 61
# MissingResponseError:
# Attempting 62
# MissingResponseError:
# Attempting 63
# bytearray(b'0\x01?')
# Attempting 64
# bytearray(b'0\x01@')
# Attempting 65
# bytearray(b'0\x01A')
# Attempting 66
# bytearray(b'0\x01B')
# Attempting 67
# bytearray(b'0\x01C')
# Attempting 68
# bytearray(b'0\x01D')
# Attempting 69
# bytearray(b'0\x01E')
# Attempting 70
# bytearray(b'0\x01F')
# Attempting 71
# bytearray(b'0\x01G')
# Attempting 72
# bytearray(b'0\x01H')
# Attempting 73
# bytearray(b'0\x01I')
# Attempting 74
# bytearray(b'0\x01J')
# Attempting 75
# bytearray(b'0\x01K')
# Attempting 76
# bytearray(b'0\x01L')
# Attempting 77
# bytearray(b'0\x01M')
# Attempting 78
# bytearray(b'0\x01N')
# Attempting 79
# bytearray(b'0\x01O')
# Attempting 80
# bytearray(b'0\x01P')
# Attempting 81
# bytearray(b'0\x01Q')
# Attempting 82
# bytearray(b'0\x01R')
# Attempting 83
# bytearray(b'0\x01S')
# Attempting 84
# bytearray(b'0\x01T')
# Attempting 85
# bytearray(b'0\x01U')
# Attempting 86
# bytearray(b'0\x01V')
# Attempting 87
# bytearray(b'0\x01W')
# Attempting 88
# bytearray(b'0\x01X')
# Attempting 89
# bytearray(b'0\x01Y')
# Attempting 90
# bytearray(b'0\x01Z')
# Attempting 91
# bytearray(b'0\x01[')
# Attempting 92
# bytearray(b'0\x01\\')
# Attempting 93
# bytearray(b'0\x01]')
# Attempting 94
# bytearray(b'0\x01^')
# Attempting 95
# bytearray(b'0\x01_')
# Attempting 96
# bytearray(b'0\x01`')
# Attempting 97
# bytearray(b'0\x01a')
# Attempting 98
# bytearray(b'0\x01b')
# Attempting 99
# bytearray(b'0\x01c')
# Attempting 100
# bytearray(b'0\x01d')
# Attempting 101
# bytearray(b'0\x01e')
# Attempting 102
# bytearray(b'0\x01f')
# Attempting 103
# bytearray(b'0\x01g')
# Attempting 104
# bytearray(b'0\x01h')
# Attempting 105
# bytearray(b'0\x01i')
# Attempting 106
# bytearray(b'0\x01j')
# Attempting 107
# bytearray(b'0\x01k')
# Attempting 108
# bytearray(b'0\x01l')
# Attempting 109
# bytearray(b'0\x01m')
# Attempting 110
# bytearray(b'0\x01n')
# Attempting 111
# bytearray(b'0\x01o')
# Attempting 112
# bytearray(b'0\x01p')
# Attempting 113
# bytearray(b'0\x01q')
# Attempting 114
# bytearray(b'0\x01r')
# Attempting 115
# bytearray(b'0\x01s')
# Attempting 116
# bytearray(b'0\x01t')
# Attempting 117
# bytearray(b'0\x01u')
# Attempting 118
# bytearray(b'0\x01v')
# Attempting 119
# bytearray(b'0\x01w')
# Attempting 120
# bytearray(b'0\x01x')
# Attempting 121
# bytearray(b'0\x01y')
# Attempting 122
# bytearray(b'0\x01z')
# Attempting 123
# bytearray(b'0\x01{')
# Attempting 124
# bytearray(b'0\x01|')
# Attempting 125
# bytearray(b'0\x01}')
# Attempting 126
# bytearray(b'0\x01~')
# Attempting 127
# bytearray(b'0\x01\x7f')
# Attempting 128
# bytearray(b'0\x01\x80')
# Attempting 129
# bytearray(b'0\x01\x81')
# Attempting 130
# bytearray(b'0\x01\x82')
# Attempting 131
# bytearray(b'0\x01\x83')
# Attempting 132
# bytearray(b'0\x01\x84')
# Attempting 133
# bytearray(b'0\x01\x85')
# Attempting 134
# bytearray(b'0\x01\x86')
# Attempting 135
# bytearray(b'0\x01\x87')
# Attempting 136
# bytearray(b'0\x01\x88')
# Attempting 137
# bytearray(b'0\x01\x89')
# Attempting 138
# bytearray(b'0\x01\x8a')
# Attempting 139
# bytearray(b'0\x01\x8b')
# Attempting 140
# bytearray(b'0\x01\x8c')
# Attempting 141
# bytearray(b'0\x01\x8d')
# Attempting 142
# bytearray(b'0\x01\x8e')
# Attempting 143
# bytearray(b'0\x01\x8f')
# Attempting 144
# bytearray(b'0\x01\x90')
# Attempting 145
# bytearray(b'0\x01\x91')
# Attempting 146
# bytearray(b'0\x01\x92')
# Attempting 147
# bytearray(b'0\x01\x93')
# Attempting 148
# bytearray(b'0\x01\x94')
# Attempting 149
# bytearray(b'0\x01\x95')
# Attempting 150
# bytearray(b'0\x01\x96')
# Attempting 151
# bytearray(b'0\x01\x97')
# Attempting 152
# bytearray(b'0\x01\x98')
# Attempting 153
# bytearray(b'0\x01\x99')
# Attempting 154
# bytearray(b'0\x01\x9a')
# Attempting 155
# bytearray(b'0\x01\x9b')
# Attempting 156
# bytearray(b'0\x01\x9c')
# Attempting 157
# bytearray(b'0\x01\x9d')
# Attempting 158
# bytearray(b'0\x01\x9e')
# Attempting 159
# bytearray(b'0\x01\x9f')
# Attempting 160
# bytearray(b'0\x01\xa0')
# Attempting 161
# bytearray(b'0\x01\xa1')
# Attempting 162
# bytearray(b'0\x01\xa2')
# Attempting 163
# bytearray(b'0\x01\xa3')
# Attempting 164
# bytearray(b'0\x01\xa4')
# Attempting 165
# bytearray(b'0\x01\xa5')
# Attempting 166
# bytearray(b'0\x01\xa6')
# Attempting 167
# bytearray(b'0\x01\xa7')
# Attempting 168
# bytearray(b'0\x01\xa8')
# Attempting 169
# bytearray(b'0\x01\xa9')
# Attempting 170
# bytearray(b'0\x01\xaa')
# Attempting 171
# bytearray(b'0\x01\xab')
# Attempting 172
# bytearray(b'0\x01\xac')
# Attempting 173
# bytearray(b'0\x01\xad')
# Attempting 174
# bytearray(b'0\x01\xae')
# Attempting 175
# bytearray(b'0\x01\xaf')
# Attempting 176
# bytearray(b'0\x01\xb0')
# Attempting 177
# bytearray(b'0\x01\xb1')
# Attempting 178
# bytearray(b'0\x01\xb2')
# Attempting 179
# bytearray(b'0\x01\xb3')
# Attempting 180
# bytearray(b'0\x01\xb4')
# Attempting 181
# bytearray(b'0\x01\xb5')
# Attempting 182
# bytearray(b'0\x01\xb6')
# Attempting 183
# bytearray(b'0\x01\xb7')
# Attempting 184
# bytearray(b'0\x01\xb8')
# Attempting 185
# bytearray(b'0\x01\xb9')
# Attempting 186
# bytearray(b'0\x01\xba')
# Attempting 187
# bytearray(b'0\x01\xbb')
# Attempting 188
# bytearray(b'0\x01\xbc')
# Attempting 189
# bytearray(b'0\x01\xbd')
# Attempting 190
# bytearray(b'0\x01\xbe')
# Attempting 191
# bytearray(b'0\x01\xbf')
# Attempting 192
# bytearray(b'0\x01\xc0')
# Attempting 193
# bytearray(b'0\x01\xc1')
# Attempting 194
# bytearray(b'0\x01\xc2')
# Attempting 195
# bytearray(b'0\x01\xc3')
# Attempting 196
# bytearray(b'0\x01\xc4')
# Attempting 197
# bytearray(b'0\x01\xc5')
# Attempting 198
# bytearray(b'0\x01\xc6')
# Attempting 199
# bytearray(b'0\x01\xc7')
# Attempting 200
# bytearray(b'0\x01\xc8')
# Attempting 201
# bytearray(b'0\x01\xc9')
# Attempting 202
# bytearray(b'0\x01\xca')
# Attempting 203
# bytearray(b'0\x01\xcb')
# Attempting 204
# bytearray(b'0\x01\xcc')
# Attempting 205
# bytearray(b'0\x01\xcd')
# Attempting 206
# bytearray(b'0\x01\xce')
# Attempting 207
# bytearray(b'0\x01\xcf')
# Attempting 208
# bytearray(b'0\x01\xd0')
# Attempting 209
# bytearray(b'0\x01\xd1')
# Attempting 210
# bytearray(b'0\x01\xd2')
# Attempting 211
# bytearray(b'0\x01\xd3')
# Attempting 212
# bytearray(b'0\x01\xd4')
# Attempting 213
# bytearray(b'0\x01\xd5')
# Attempting 214
# bytearray(b'0\x01\xd6')
# Attempting 215
# bytearray(b'0\x01\xd7')
# Attempting 216
# bytearray(b'0\x01\xd8')
# Attempting 217
# bytearray(b'0\x01\xd9')
# Attempting 218
# bytearray(b'0\x01\xda')
# Attempting 219
# bytearray(b'0\x01\xdb')
# Attempting 220
# bytearray(b'0\x01\xdc')
# Attempting 221
# bytearray(b'0\x01\xdd')
# Attempting 222
# bytearray(b'0\x01\xde')
# Attempting 223
# bytearray(b'0\x01\xdf')
# Attempting 224
# bytearray(b'0\x01\xe0')
# Attempting 225
# bytearray(b'0\x01\xe1')
# Attempting 226
# bytearray(b'0\x01\xe2')
# Attempting 227
# bytearray(b'0\x01\xe3')
# Attempting 228
# bytearray(b'0\x01\xe4')
# Attempting 229
# bytearray(b'0\x01\xe5')
# Attempting 230
# bytearray(b'0\x01\xe6')
# Attempting 231
# bytearray(b'0\x01\xe7')
# Attempting 232
# bytearray(b'0\x01\xe8')
# Attempting 233
# bytearray(b'0\x01\xe9')
# Attempting 234
# bytearray(b'0\x01\xea')
# Attempting 235
# bytearray(b'0\x01\xeb')
# Attempting 236
# bytearray(b'0\x01\xec')
# Attempting 237
# bytearray(b'0\x01\xed')
# Attempting 238
# bytearray(b'0\x01\xee')
# Attempting 239
# bytearray(b'0\x01\xef')
# Attempting 240
# bytearray(b'0\x01\xf0')
# Attempting 241
# bytearray(b'0\x01\xf1')
# Attempting 242
# bytearray(b'0\x01\xf2')
# Attempting 243
# bytearray(b'0\x01\xf3')
# Attempting 244
# bytearray(b'0\x01\xf4')
# Attempting 245
# bytearray(b'0\x01\xf5')
# Attempting 246
# bytearray(b'0\x01\xf6')
# Attempting 247
# bytearray(b'0\x01\xf7')
# Attempting 248
# bytearray(b'0\x01\xf8')
# Attempting 249
# bytearray(b'0\x01\xf9')
# Attempting 250
# bytearray(b'0\x01\xfa')
# Attempting 251
# bytearray(b'0\x01\xfb')
# Attempting 252
# bytearray(b'0\x01\xfc')
# Attempting 253
# bytearray(b'0\x01\xfd')
# Attempting 254
# bytearray(b'0\x01\xfe')
# Attempting 255
# bytearray(b'0\x01\xff')