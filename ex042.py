r1 = float(input('Tamanho da primeira reta: '))
r2 = float(input('Tamanho da segunda reta: '))
r3 = float(input('Tamanho da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Com esses valores é possivel formar um {}TRIÂNGULO EQUILÁTERO{}.'.format('\033[4;32m', '\033[m'))
    elif r1 == r2 and r1 != r3 and r2 != r3 or r1 == r3 and r1 != r2 and r2 != r3 or r2 == r3 and r2 != r1 and r3 != r1:
        print('Com esses valores é possível formar um {}TRIÂNGULO ISÓSCELES{}.'.format('\033[4;32m', '\033[m'))
    elif r1 != r2 != r3 != r1:
        print('Com esses valores é possível formar um {}TRIÂNGULO ESCALENO{}.'.format('\033[4;32m', '\033[m'))
else:
    print('Com esses valores {}NÃO{} é possível formar um {}TRIÂNGULO{}.'.format('\033[4;31m', '\033[m', '\033[4;31m', '\033[m'))
