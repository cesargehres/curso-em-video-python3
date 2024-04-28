Programa = True
v1 = int(input('Primeiro valor:'))
v2 = int(input('Segundo valor:'))
while Programa == True:
    op = int(input('[1] Somar\n'
                   '[2] Multiplicar\n'
                   '[3] Maior\n'
                   '[4] Novos Números\n'
                   '[5] Sair do Programa\n'
                   'Escolha Uma Opção:'))
    if op == 1:
        print(v1 + v2)
    elif op == 2:
        print(v1 * v2)
    elif op == 3:
        if v1 > v2:
            print('{} é Maior'.format(v1))
        elif v1 < v2:
            print('{} é Maior'.format(v2))
        else:
            print('{} e {} são equivalentes'.format(v1,v2))
    elif op == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif op == 5:
        Programa = False
    else:
        print('Escolha uma opção válida.')
