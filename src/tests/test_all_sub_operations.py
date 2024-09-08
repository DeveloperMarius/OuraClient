from oura import OuraClient
from oura.exceptions.missing_response_error import MissingResponseError
import asyncio

async def main():
    auth_key = bytes.fromhex("324e29504887dc73f2de912fa2274522")
    async with OuraClient("A0:38:F8:37:5E:00", auth_key) as client:
        for i in range(0x0, 63):
            if i in [26]:
                continue
            print(f'Attempting Operation {i}')
            for i2 in range(0x00, 0x100):
                print(f'Attempting Sub Operation {i2}')
                try:
                    response = await client.raw_request(bytes([i, 0x1, i2]))
                    print(f'Response: {response}')
                except MissingResponseError as e:
                    print(f'MissingResponseError: {e}')
                except Exception as e:
                    print(f'Error: {e}')
                    exit()

asyncio.run(main())


# Not found error: bytearray(b'0\x01\xf1')
# Fehler = Missing Response
# v = await client.raw_request(bytes([47, 0x0]))
# print(v)
    # auth_key = bytes.fromhex("324e29504887dc73f2de912fa2274588")
# Connecting...
# Connected
# Paired: True
# Received nonce: f155688a450f36ee8a61418598d7ed
# Authenticated with ring!
# Attempting Operation 47
# Attempting Sub Operation 0
# Response: bytearray(b'/\x02\x00\x00')
# Attempting Sub Operation 1
# MissingResponseError:
# Attempting Sub Operation 2
# Response: bytearray(b'/\x02\x00\x02')
# Attempting Sub Operation 3
# MissingResponseError:
# Attempting Sub Operation 4
# Response: bytearray(b'/\x02\x00\x04')
# Attempting Sub Operation 5
# Response: bytearray(b'/\x02\x00\x05')
# Attempting Sub Operation 6
# Response: bytearray(b'/\x02\x00\x06')
# Attempting Sub Operation 7
# Response: bytearray(b'/\x02\x00\x07')
# Attempting Sub Operation 8
# Response: bytearray(b'/\x02\x00\x08')
# Attempting Sub Operation 9
# Response: bytearray(b'/\x02\x00\t')
# Attempting Sub Operation 10
# Response: bytearray(b'/\x02\x00\n')
# Attempting Sub Operation 11
# Response: bytearray(b'/\x02\x00\x0b')
# Attempting Sub Operation 12
# Response: bytearray(b'/\x02\x00\x0c')
# Attempting Sub Operation 13
# Response: bytearray(b'/\x02\x00\r')
# Attempting Sub Operation 14
# Response: bytearray(b'/\x02\x00\x0e')
# Attempting Sub Operation 15
# Response: bytearray(b'/\x02\x00\x0f')
# Attempting Sub Operation 16
# Response: bytearray(b'/\x02\x00\x10')
# Attempting Sub Operation 17
# Response: bytearray(b'/\x02\x00\x11')
# Attempting Sub Operation 18
# Response: bytearray(b'/\x02\x00\x12')
# Attempting Sub Operation 19
# Response: bytearray(b'/\x02\x00\x13')
# Attempting Sub Operation 20
# Response: bytearray(b'/\x02\x00\x14')
# Attempting Sub Operation 21
# Response: bytearray(b'/\x02\x00\x15')
# Attempting Sub Operation 22
# Response: bytearray(b'/\x02\x00\x16')
# Attempting Sub Operation 23
# Response: bytearray(b'/\x02\x00\x17')
# Attempting Sub Operation 24
# Response: bytearray(b'/\x02\x00\x18')
# Attempting Sub Operation 25
# Response: bytearray(b'/\x02\x00\x19')
# Attempting Sub Operation 26
# Response: bytearray(b'/\x02\x00\x1a')
# Attempting Sub Operation 27
# Response: bytearray(b'/\x02\x00\x1b')
# Attempting Sub Operation 28
# Response: bytearray(b'/\x02\x00\x1c')
# Attempting Sub Operation 29
# Response: bytearray(b'/\x02\x00\x1d')
# Attempting Sub Operation 30
# Response: bytearray(b'/\x02\x00\x1e')
# Attempting Sub Operation 31
# Response: bytearray(b'/\x02\x00\x1f')
# Attempting Sub Operation 32
# MissingResponseError:
# Attempting Sub Operation 33
# Response: bytearray(b'/\x02\x00!')
# Attempting Sub Operation 34
# MissingResponseError:
# Attempting Sub Operation 35
# Response: bytearray(b'/\x02\x00#')
# Attempting Sub Operation 36
# MissingResponseError:
# Attempting Sub Operation 37
# Response: bytearray(b'/\x02\x00%')
# Attempting Sub Operation 38
# MissingResponseError:
# Attempting Sub Operation 39
# Response: bytearray(b"/\x02\x00\'")
# Attempting Sub Operation 40
# Response: bytearray(b'/\x02\x00(')
# Attempting Sub Operation 41
# MissingResponseError:
# Attempting Sub Operation 42
# Response: bytearray(b'/\x02\x00*')
# Attempting Sub Operation 43
# Response: bytearray(b'/\x10,\x07\x13\xa82)\x13\xaa/\xf0\xb3{\xf7|\x129')
# Attempting Sub Operation 44
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 45
# MissingResponseError:
# Attempting Sub Operation 46
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 47
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 48
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 49
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 50
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 51
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 52
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 53
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 54
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 55
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 56
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 57
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 58
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 59
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 60
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 61
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 62
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 63
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 64
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 65
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 66
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 67
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 68
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 69
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 70
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 71
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 72
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 73
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 74
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 75
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 76
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 77
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 78
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 79
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 80
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 81
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 82
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 83
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 84
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 85
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 86
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 87
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 88
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 89
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 90
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 91
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 92
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 93
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 94
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 95
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 96
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 97
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 98
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 99
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 100
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 101
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 102
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 103
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 104
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 105
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 106
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 107
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 108
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 109
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 110
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 111
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 112
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 113
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 114
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 115
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 116
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 117
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 118
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 119
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 120
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 121
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 122
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 123
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 124
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 125
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 126
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 127
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 128
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 129
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 130
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 131
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 132
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 133
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 134
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 135
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 136
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 137
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 138
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 139
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 140
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 141
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 142
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 143
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 144
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 145
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 146
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 147
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 148
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 149
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 150
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 151
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 152
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 153
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 154
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 155
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 156
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 157
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 158
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 159
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 160
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 161
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 162
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 163
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 164
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 165
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 166
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 167
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 168
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 169
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 170
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 171
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 172
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 173
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 174
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 175
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 176
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 177
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 178
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 179
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 180
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 181
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 182
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 183
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 184
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 185
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 186
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 187
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 188
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 189
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 190
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 191
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 192
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 193
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 194
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 195
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 196
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 197
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 198
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 199
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 200
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 201
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 202
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 203
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 204
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 205
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 206
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 207
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 208
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 209
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 210
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 211
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 212
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 213
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 214
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 215
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 216
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 217
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 218
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 219
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 220
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 221
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 222
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 223
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 224
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 225
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 226
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 227
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 228
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 229
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 230
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 231
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 232
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 233
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 234
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 235
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 236
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 237
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 238
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 239
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 240
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 241
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 242
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 243
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 244
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 245
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 246
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 247
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 248
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 249
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 250
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 251
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 252
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 253
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 254
# Response: bytearray(b'/\x02/\x01')
# Attempting Sub Operation 255
# Response: bytearray(b'/\x02/\x01')