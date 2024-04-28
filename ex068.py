from random import randint
ce = ''
v = 0
print(24*'-')
print('Vamos jogar par ou impar')
print(24*'-')
while True:
    je = str(input('Escolha Par ou Ímpar[P/I]: ')).strip().upper()
    while je not in ('P','I'):
        je = str(input('Escolha inválida,tente novamente[P/I]: ')).strip().upper()
    if je == 'P':
        je = 'Par'
        ce = 'Ímpar'
    elif je == 'I':
        je = 'Ímpar'
        ce = 'Par'
    nj = int(input('Escolha um número: '))
    nc = randint(1, 10)
    r = (nj + nc) % 2
    if je == 'Par' and r == 0 or je == 'Ímpar' and r != 0:
        v += 1
        print(5*'-', 'Você Ganhou!', 5*'-')
        print(f'Jogador: {je} / {nj}')
        print(f'Computador: {ce} / {nc}')
        print(f'{nj + nc} é Par' if r == 0 else f'{nj + nc} é Ímpar')
        print(f'Número de vitórias: {v}')
    else:
        print(5 * '-', 'Você Perdeu!', 5 * '-')
        print(f'Jogador escolheu: {je} / {nj}')
        print(f'Computador: {ce} / {nc}')
        print(f'{nj + nc} é Par' if r == 0 else f'{nj + nc} é Ímpar')
        if v > 1:
            print(f'Você ganhou {v} vezes.')
        else:
            print(f'Você ganhou {v} vez.' if v == 1 else 'Você nao ganhou nenhuma vez.')
        newgame = str(input('Quer tentar novamente?[S/N] ')).strip().upper()
        if newgame == 'N':
            break
        elif newgame != 'S':
            while newgame != 'S':
                newgame = str(input('Quer tentar novamente?[S/N] ')).strip().upper()
