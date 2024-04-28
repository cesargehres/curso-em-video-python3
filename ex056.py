NomeHV = str('')
HomemV = 0
Homens = 0
Idade = 0
MediaIdade = 0
Mulheres19 = 0
for p in range(1, 5):
    Nome = str(input('Nome:')).strip()
    Sexo = str(input('Sexo[M/F]:')).strip().upper()
    Idade = int(input('Idade:'))
    MediaIdade += Idade / p
    if Sexo == 'M':
        Homens += 1
    if Sexo == 'M' and HomemV < Idade:
        HomemV = Idade
        NomeHV = Nome
    elif Sexo == 'F' and Idade < 20:
        Mulheres19 += 1
if Homens != 0:
    print('O homem mais velho se chama {}.'.format(NomeHV))
    print('Existem {} mulherer(s) com menos de 20 anos.'.format(Mulheres19))
    print('A média de idade do grupo é de {} anos.'.format(int(MediaIdade)))
else:
    print('Não há nenhum homem no grupo.')
    print('Existem {} mulherer(s) com menos de 20 anos.'.format(Mulheres19))
    print('A média de idade do grupo é de {} anos.'.format(int(MediaIdade)))
