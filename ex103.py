def ficha(nome='<desconhecido>', gols='0'):
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = int(0)
    return(f'O Jogador {nome} fez {gols} gol(s) no capeonato.')


#Programa principal
nome = str(input('Nome do Jogador: ')).title().strip()
gols = str(input('Número de Gols: '))
print(ficha(nome, gols))
