Jogador = {'Nome': str(input('Nome: ')).title().strip(),
           'Partidas': int(input('Partidas jogadas: ')),
           'Gols/Partida': [],
           'Total/Gols': int(0)}

for c in range(1, Jogador['Partidas'] + 1):
    Jogador['Gols/Partida'].append(int(input(f'Gols na {c}° partida: ')))
for v in Jogador['Gols/Partida']:
    Jogador['Total/Gols'] += v

print('-=' * 35)
print(Jogador)

print(35 * '-=')
for k, v in Jogador.items():
    print(f'{k}: {v}')

print(35 * '-=')
print(f'O jogador {Jogador["Nome"]} jogou {Jogador["Partidas"]} partidas.')
c = 1
for v in Jogador['Gols/Partida']:
    print(f'   ==> Gols na {c}° partida: {v}')
    c += 1
print(f' --- Foi um total de {Jogador["Total/Gols"]} gols. ---')