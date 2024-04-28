l = [[], [], []]
for c in range(0, 3):
    l[0].append(int(input(f'Digite um valor para[{c}, 0]: ')))
    l[1].append(int(input(f'Digite um valor para[{c}, 0]: ')))
    l[2].append(int(input(f'Digite um valor para[{c}, 0]: ')))
for v in l[0]:
    print(f'[ {v:^5}', end=' ]')
print(f'\n', end='')
for v in l[1]:
    print(f'[ {v:^5}', end=' ]')
print(f'\n', end='')
for v in l[2]:
    print(f'[ {v:^5}', end=' ]')
