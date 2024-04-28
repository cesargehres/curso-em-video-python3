def LeiaDinheiro(msg):
    erro = True
    while erro == True:
        n = input(msg).replace(',', '.').strip()
        if n.isalpha() or n in '':
            print('\033[31m' + 'Erro' + '\033[m')
        else:
            return float(n)
