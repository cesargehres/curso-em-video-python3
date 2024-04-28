m19 = 0   #Mulheres com menos de 20 anos
p18 = 0   #Pessoas com menos de 18 anos
counth = 0   #Contagem de homens
while True:
    nome = str(input('Nome: ')).strip().upper()
    sexo = str(input('Sexo[M/F]: ')).strip().upper()
    while sexo not in ('M', 'F'):
        sexo = str(input('Por favor digite um valor válido[M/F]: ')).strip().upper()
    idade = int(input('Idade: '))
    if sexo == 'F' and idade < 20:
        m19 += 1
    if sexo == 'M':
        counth += 1
    if idade >= 18:
        p18 += 1
    continuar = str(input('Quer continuar?[S/N] ')).strip().upper()
    while continuar not in ('S', 'N'):
        continuar = str(input('Por favor digite um valor valido[S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'No grupo há {counth} homens.')
print(f'No grupo há {m19} mulheres com menos de 20 anos.')
print(f'No grupo há {p18} pessoas maiores de 18 anos.')
