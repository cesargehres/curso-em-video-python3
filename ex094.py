lista = list()
Midd = list() #Média de idade
LM = list() #Lista de mulheres
while True:
    pessoa = {'Nome': str(input('Nome: ')).strip().title()}
    pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while pessoa['Sexo'] not in ('M', 'F'):
        pessoa['Sexo'] = str(input('Valor inválido,digite [M] para masculino ou [F] para feminino'))
    pessoa['Idade'] = int(input('Idade: '))
    Midd.append(pessoa['Idade'])
    lista.append(pessoa.copy())
    if pessoa['Sexo'] == 'F':
        LM.append(pessoa.copy())
    continuar = str(input('Quer continuar? [S/N] '))
    while continuar not in ('S', 's', 'N', 'n'):
        continuar = str(input('Valor inválido,digite [S] para continuar ou [N] para parar.'))
    if continuar in ('N', 'n'):
        break
Midd = int(sum(Midd) / len(lista))

print(40 * '-=')
print(f'No total foram cadastradas {len(lista)} pessoas.')
print(f'A média de idade é {Midd} anos.')
print('Mulheres cadastradas: ', end='')
for c in range(0, len(LM)):
    if c < len(LM) - 1:
        print(f'{LM[c]["Nome"]}', end=', ')
    elif c == len(LM) - 1:
        print(f'{LM[c]["Nome"]}.')
print(f'Pesooas com idade acima de {Midd} anos: ', end='')
for v in lista:
    if v['Idade'] > Midd:
        if v != lista[len(lista) - 1]:
            print(f'{v["Nome"]} com {v["Idade"]} anos, ', end='')
        else:
            print(f'{v["Nome"]} com {v["Idade"]} anos.')
