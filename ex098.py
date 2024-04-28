from time import sleep
def contador(i, f, p):
    if i < f:
        f += 1
        if p < 0:
            p = -p
    elif i > f:
        f -= 1
        if p > 0:
            p = -p
    if p == 0:
        if f > i:
            p = 1
        elif f < i:
            p = -1
    for c in range(i, f, p):
        sleep(0.25)
        if p > 0:
            print(f'{c}, ' if c < f - p else f'{c}.', end='')
        elif p < 0:
            print(f'{c}, ' if c > f - p else f'{c}.', end='')
    print()


print('Contagem de 1 até 10 com passo em 1.')
contador(1, 10, 1)
print(30 * '-=')
print('Contagem de 10 até 0 com passo em 2.')
contador(10, 0, 1)
print(30 * '-=')
print('Contagem Personalizada.')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print(30 * '-=')
print(f'Contagem de {i} até {f} com passo em {p}.')
contador(i, f, p)
