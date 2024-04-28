print('Gerador de PA')
PT = int(input('Primeiro termo: '))
R = int(input('Razão da PA: '))
c = 0
print('{} ->'.format(PT), end='')
while c < 9:
    PT += R
    print(' {} ->'.format(PT), end='')
    c += 1
print(' fim')
