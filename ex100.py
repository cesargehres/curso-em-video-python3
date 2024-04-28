from random import randint

def sorteia(n, lista):
    for c in range(0, n):
        lista.append(randint(0, 100))


def somaPar(lista):
    c = 0
    print(f'Números pares: ', end='')
    for v in lista:
        if v % 2 == 0:
            print(f'{v} ', end='')
            c += v
    print()
    print(f'Resultado da soma entre os pares: {c}')


#Programa Principal
lista = []
sorteia(7, lista)
print(f'Os números sorteados: {lista}')
somaPar(lista)
