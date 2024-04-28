n = int(input('Digite um número para ver seu fatorial: '))
f = 1
print('{}! '.format(n), end='')
for c in range(n, 0, -1):
    f *= c
    print('{} x '.format(c) if c > 1 else '1 = {}'.format(f), end='')
