from ex115a.lib import cor

def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print(cor.vermelho('ERRO! Por favor digite um número inteiro válido!'))
        except KeyboardInterrupt:
            print(cor.vermelho('\nO usuário preferiu não digitar o número.'))
            return 'Número não informado'
        else:
            return n
