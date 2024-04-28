import time
import random

    #Sorteio dos jogos
ljogos = []
jogo = []
print(20 * '-=')
print(f'''{'JOGO NA MEGA SENA':^40}''')
print(20 * '-=')
nj = int(input('Quantos jogos você quer sortear? '))
for c in range(1, nj + 1):
    for j in range(0, 6):
        n = random.randint(1, 60)
        if n in jogo:
            while n in jogo:
                n = random.randint(1, 60)
        jogo.append(n)
    jogo.sort()
    ljogos.append(jogo[:])
    jogo.clear()

    #Resultado dos jogos
print(40 * '-')
print(f'''{f'SORTEANDO {nj} JOGOS...':^40}''')
print(40 * '-')
for l in range(0, nj):
    time.sleep(0.75)
    for c in range(0, 6):
        if c == 0:
            print(f'Jogo {l + 1}:[{ljogos[l][c]:>2},', end='')
        else:
            print(f'{ljogos[l][c]:>3},' if c < 5 else f'{ljogos[l][c]:>3}]', end='')
    print()
