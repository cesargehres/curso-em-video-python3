matriz = [list(), list(), list()]
sdp = s3c = mn = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para[{l}, {c}]: ')))
print(30*'-')
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            sdp += matriz[l][c]
        print(f'[ {matriz[l][c]:^5} ]', end='')
    print()
print(30*'-')
print(f'A soma de todos os pares é: {sdp}')
for v in matriz:
    s3c += v[2]
print(f'A soma dos valores da terceira coluna é: {s3c}')
for v in matriz[1]:
    if v == matriz[1][0]:
        mn = v
    elif v > mn:
        mn = v
print(f'O maior valor da segunda linha é: {mn}')
