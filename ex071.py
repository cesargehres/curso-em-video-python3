cinquenta = vinte = dez = um = 0
vs = vss = int(input('Qual valor deseja sacar? R$ '))
while vss >= 50:
    cinquenta += 1
    vss -= 50
while vss >= 20:
    vinte += 1
    vss -= 20
while vss >= 10:
    dez += 1
    vss -= 10
while vss >= 1:
    um += 1
    vss -= 1
print(f'Você sacou R$ {vs},00.')
print('Serão entregues:')
if cinquenta > 0:
    print(f'{cinquenta} cédula(s) de 50,00.')
if vinte > 0:
    print(f'{vinte} cédula(s) de 20,00.')
if dez > 0:
    print(f'{dez} cédula(s) de 10,00.')
if um > 0:
    print(f'{um} cédula(s) de R$ 1,00.')
