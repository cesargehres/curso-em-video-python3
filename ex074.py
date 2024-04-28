from random import randint
nums_aleatorios = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print('Números:')
for c in range(0, len(nums_aleatorios)):
    print(f'{nums_aleatorios[c]}', end=' ')
print(f'\nO menor número é {min(nums_aleatorios)}')
print(f'O maior número é {max(nums_aleatorios)}')
