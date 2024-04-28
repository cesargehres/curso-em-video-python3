from random import randint

j = dict()
for c in range(1, 5):
    j[f'Jogador {c}'] = int(randint(1, 6))
c = 1
for jo in sorted(j, key=j.get, reverse=True):
    print(f'{c}° lugar: ', end='')
    print(f'{jo} com {j[jo]} pontos.')
    c += 1
