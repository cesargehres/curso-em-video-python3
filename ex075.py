n = (int(input('Digite o 1° número: ')),
     int(input('Digite o 2° número: ')),
     int(input('Digite o 3° número: ')),
     int(input('Digite o ultimo número: ')))
if 3 in n:
    print(f'O número 3 esta localizado na {n.index(3) + 1} posição')
else:
    print('O número 3 não foi digitado')
print(f'O número 9 apareceu {n.count(9)} vez(es)')
print('Os números pares são:', end=' ')
for p in n:
    if p % 2 == 0:
        print(f'{p}', end=' ')
