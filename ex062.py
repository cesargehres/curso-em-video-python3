print('Progressão Aritmética')
pt = int(input('Primeiro Termo:'))
r = int(input('Razão: '))
count = pt
count2= 10
print('{} -> '.format(pt), end='')
for c in range(1, 10):
    count += r
    print('{} -> '.format(count), end='')
te = 1
while te != 0:
    te = int(input('\nQuantos termos você quer mostrar a mais? '))
    count2 += te
    for c2 in range(0, te):
        count += r
        print('{} -> '.format(count), end='')
print('\nA Progressão acabou com {} termos mostrados.'.format(count2))
