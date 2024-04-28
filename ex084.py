pessoa = []
dados = []
while True:
    dados.append(str(input('Nome:')).strip().title())
    dados.append(int(input('Peso:')))
    pessoa.append(dados[:])
    dados.clear()
    while True:
        con = str(input('Quer continuar?(S/N)'))
        if con.upper() in 'S':
            break
        if con.upper() in 'N':
            break
    if con.upper() in 'N':
        break

pmen = []
pmai = []
for p in pessoa:
    if p[1] < 70:
        pmen.append(p[0])
    elif p[1] > 100:
        pmai.append(p[0])
print(f'Foram cadastradas {len(pessoa)} pessoas.')
print(f'Pessoas com menos de 70 Kg: {pmen}')
print(f'Pessoas com mais de 100 Kg: {pmai}')
