maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}° pessoa:(kg) '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
print('{}kg é o maior peso.'.format(maior))
print('{}kg é o menor peso.'.format(menor))
