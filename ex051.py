print('=' * 31)
print('     DEZ TERMOS DE UMA PA')
print('=' * 31)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
count = pt
print('{}'.format(pt), end=' -> ')
for c in range(0, 9):
    count += r
    print('{}'.format(count), end=' -> ')
print('ACABOU!')
