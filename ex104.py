def leiaInt(msg):
    cor = {'red': '\033[0;31m', 'default': '\033[m'}
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print(f'{cor["red"]}ERRO! Digite um número inteiro válido.{cor["default"]}')
    return valor


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
