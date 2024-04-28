from random import randint
print('Suas opções:')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
j = int(input('Qual é sua jogada? '))
ia = randint(1, 3)
if j == 1:
    oj = 'PEDRA'
    if ia == 1:
        oia = 'PEDRA'
    elif ia == 2:
        oia = 'PAPEL'
    elif ia == 3:
        oia = 'TESOURA'
    print('JO')
    print('KEN')
    print('PO!!!')
    print('\033[1m=-' * 15)
    print('Você jogou {}'.format(oj))
    print('Computador jogou {}'.format(oia))
    if ia == j:
        print('EMPATE!')
    elif ia == 1 and j == 2 or ia == 2 and j == 3 or ia == 3 and j == 1:
        print('VOCÊ GANHOU!')
    else:
        print('O COMPUTADOR GANHOU!')
    print('\033[1m=-' * 15)
elif j == 2:
    oj = 'PAPEL'
    if ia == 1:
        oia = 'PEDRA'
    elif ia == 2:
        oia = 'PAPEL'
    elif ia == 3:
        oia = 'TESOURA'
    print('JO')
    print('KEN')
    print('PO!!!')
    print('\033[1m=-' * 15)
    print('Você jogou {}'.format(oj))
    print('Computador jogou {}'.format(oia))
    if ia == j:
        print('EMPATE!')
    elif ia == 1 and j == 2 or ia == 2 and j == 3 or ia == 3 and j == 1:
        print('VOCÊ GANHOU!')
    else:
        print('O COMPUTADOR GANHOU!')
    print('\033[1m=-' * 15)
elif j == 3:
    oj = 'TESOURA'
    if ia == 1:
        oia = 'PEDRA'
    elif ia == 2:
        oia = 'PAPEL'
    elif ia == 3:
        oia = 'TESOURA'
    print('JO')
    print('KEN')
    print('PO!!!')
    print('\033[1m=-' * 15)
    print('Você jogou {}'.format(oj))
    print('Computador jogou {}'.format(oia))
    if ia == j:
        print('EMPATE!')
    elif ia == 1 and j == 2 or ia == 2 and j == 3 or ia == 3 and j == 1:
        print('VOCÊ GANHOU!')
    else:
        print('O COMPUTADOR GANHOU!')
    print('\033[1m=-' * 15)
else:
    print('Jogada inválida,tente novamente.')