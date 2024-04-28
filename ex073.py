times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
         'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahía',
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí',
         'Ponte Preta')
print(30*'-=')
print('Lista dos times do Brasileirão:')
for c in range(0, len(times)):
    print(f'{c + 1}° {times[c]}, ' if c <= 17 else f'{c + 1}° {times[c]}.\n', end='')
print(30*'-=')
print('Os 5 primeiros colocados são: ')
for c in range(0, 5):
    print(f'{c + 1}° {times[c]}, ' if c < 4 else f'{c + 1}° {times[c]}.\n', end='',)
print(30*'-=')
print('Os 4 últimos colocados são: ')
for c in range(15, 19):
    print(f'{c + 1}° {times[c]}, ' if c < 18 else f'{c + 1}° {times[c]}.\n', end='')
print(30*'-=')
print('Times em ordem alfabética:')
timeemordem = sorted(times)
for c in range(0, 19):
    print(f'{timeemordem[c]}, ' if c < 18 else f'{timeemordem[c]}\n', end='')
print(30*'-=')
print(f'{times[7]} se encontra na 8° posição')
print(30*'-=')
