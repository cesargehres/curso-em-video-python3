n = []
for c in range(0, 5):
     n.append(int(input(f'Digite um valor para Posição {c}: ')))
print(f'Você digitou os valores {n}')
print(f'O maior valor foi {max(n)} nas posiçoes:', end=' ')
for l, v in enumerate(n):
     if v == max(n):
          print(f'{l}', end=' ')
print(f'\nO menor valor foi {min(n)} nas posições:', end=' ')
for l, v in enumerate(n):
     if v == min(n):
          print(f'{l}', end=' ')
