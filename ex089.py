MA = list()
N = list()

#Looping notas e média
while True:
    N.append(str(input('Nome: ')).title().strip())
    for c in range(1, 3):
        N.append(float(input(f'Nota {c}: ')))
    N.append((N[1] + N[2]) / 2)
    MA.append(N[:])
    N.clear()
    continuar = str(input('Quer continuar? [S/N] ')).strip()
    while continuar not in ('S', 's', 'N', 'n'):
        continuar = str(input('Valor inválido,tente novamente [S] para continuar ou [N] para parar. ')).strip()
    if continuar in ('N', 'n'):
        break
print(40 * '-=')

#looping resposta ao usuário
print(f'''{'N°.':<4}{'NOME':<25}{'MÉDIA':<3}''')
print(35 * '-')
count = 0
for l in range(0, len(MA)):
    print(f'{l + 1:<4}', end='')
    print(f'''{MA[l][0]:<25}{MA[l][3]:>5.1f}''')
print(35 * '-')
while True:
    n = str(input('Mostrar notas de qual aluno? ["P" para parar] '))
    if n in ('P', 'p'):
        break
    else:
        print(f'Notas de {MA[int(n) - 1][0]} [{MA[int(n) - 1][1]}, {MA[int(n) - 1][2]}]')
        print(35 * '-')
