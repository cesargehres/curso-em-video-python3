lista = dict()
count = 0

#looping aluno,notas e média
while True:
    aluno = {'Nome': str(input('Nome: ')).title().strip(), 'Nota 1': float(input('Nota 1: ')),
             'Nota 2': float(input('Nota 2: '))}
    aluno['Média'] = (aluno['Nota 1'] + aluno['Nota 2']) / 2
    if aluno['Média'] >= 7:
        aluno['Situação'] = 'Aprovado'
    else:
        aluno['Situação'] = 'Reprovado'
    lista[f'Aluno{count}'] = aluno.copy()
    count += 1
    continuar = str(input('Quer continuar? [S/N] '))
    while continuar not in ('S', 's', 'N', 'n'):
        continuar = str(input('Por favor digite um valor válido,[S] para continuar ou [N] para parar.'))
    if continuar in ('N', 'n'):
        break
print(40 * '-=')

c = 1
print(f'''{f'N°.':<4}{'Nome':<20}{'Média':<8}{'Situação'}''')
for aluno in lista.values():
    print(f'{c:<3} ', end='')
    c += 1
    print(f'''{aluno['Nome']:<20}{aluno['Média']:>5.1f}{aluno['Situação']:>12}''')
