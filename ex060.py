n = (int(input('Digite um número para calcular seu fatorial: ')))
c = n
f = 1
print('{}!'.format(n), end='')
while c > 0:
    print(' {} x '.format(c) if c > 1 else '1 = {}'.format(f), end='')
    f *= c
    c -= 1
