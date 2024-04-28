from ex115a.lib import cor, leia

def linha(n=42):
    return f'{n * "-"}'


def cabecalho(msg):
    print(linha())
    print(f'{msg:^42}')
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for c in range(0, len(lista)):
        print(f'{cor.amarelo(c + 1)} - {cor.azul(lista[c])}')
    print(linha())
    opc = leia.LeiaInt(cor.verde('Digite sua opção: '))
    return opc
