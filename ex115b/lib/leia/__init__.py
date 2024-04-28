from ex115a.lib import cor

def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(cor.vermelho('ERRO! Por favor digite um número inteiro válido!'))
        except KeyboardInterrupt:
            print(cor.vermelho('\nO usuário preferiu não digitar o número.'))
            return 'Número não informado'
        else:
            return n


def LeiaNome(msg):
    while True:
        n = str(input(msg)).strip().title()
        if n.istitle() is True:
            return n
        else:
            print(cor.vermelho('ERRO! Digite um nome válido!'))
