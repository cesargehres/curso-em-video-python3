L = [list(), list(), list()]
for c in range(0, 7):
    n = int(input('Digite um número: '))
    L[0].append(n)
    if n % 2 == 0:
        L[1].append(n)
    else:
        L[2].append(n)
print(30*'-')
print(f'Todos os números em ordem: ')
print(f'{sorted(L[0])}')
print(f'Números pares: ')
print(f'{sorted(L[1])}')
print(f'Números ímpares: ')
print(f'{sorted(L[2])}')
