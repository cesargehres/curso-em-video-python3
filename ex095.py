L = list()
while True:
    J = {'Nome' : str(input('Nome: ')).strip().title(),
         'Partidas': int(input('Partidas jogadas: ')),
         'Gols/Partida': [],
         'Total/Gols': int(0)}
    for p in range(1, J['Partidas'] + 1):
        J['Gols/Partida'].append(int(input(f'Gols na {p}°: ')))
        J['Total/Gols'] = sum(J['Gols/Partida'])
    L.append(J.copy())
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in ('S', 'N'):
        continuar = str(input(('Valor inválido! Digite apenas [S] ou [N].'))).strip().upper()
    if continuar in ('N'):
        break

print(40 * '-=')
print(F'{"N°":<4} {"NOME/JOGADOR":<25} {"PARTIDAS":<8}   {"TOTAL/GOLS":<10}')
for c in range(0, len(L)):
    print(f'{c + 1:<4} {L[c]["Nome"]:<25} {L[c]["Partidas"]:>8}  {L[c]["Total/Gols"]:>10}')

while True:
    n = input('Digite o N° do jogador para verificar os detalhes: (Digite [P] para parar) ')
    if n in (str('P'), str('p')):
        break
    else:
        print(40 * '-=')
        n = int(n) - 1
        print(f'O jogador {L[int(n)]["Nome"]} jogou {L[int(n)]["Partidas"]} jogos.')
        for c in range(0, len(L[int(n)]['Gols/Partida'])):
            print(f'{1 * " "}==> Na {c + 1}° partida fez {L[int(n)]["Gols/Partida"][c]} gols.')
        print(f'Foi um total de {L[int(n)]["Total/Gols"]} gols.')
        print(40 * '-=')
