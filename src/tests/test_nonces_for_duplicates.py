import json

counter = {}
with open('nonces.json', 'r') as file:
    nonces = json.loads(file.read())
    for nonce in nonces:
        counter[nonce] = counter.get(nonce, 0) + 1
        if counter[nonce] > 1:
            print(f'Duplicate nonce: {nonce}')
