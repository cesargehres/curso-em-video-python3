def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('\033[31m' + 'ERRO!Por favor, digite um número inteiro válido!' + '\033[m')
        except KeyboardInterrupt:
            n = '\033[31m' + 'Número não informado.' + '\033[m'
            print('\033[31m' + 'O usuario preferiu não informar o número!' + '\033[m')
            return n
        else:
            return n


def LeiaReal(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except ValueError:
            print('\033[31m' + 'ERRO!Por favor, digite um número real válido!' + '\033[m')
        except KeyboardInterrupt:
            n = '\033[31m' + 'Número não informado' + '\033[m'
            print('\033[31m' + 'O usuario preferiu não informar o número!' + '\033[m')
            return n
        else:
            return n
