n = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
     'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito','Dezenove', 'Vinte')
while True:
    ne = int(input('Escolha um número de 0 à 20: '))
    while ne not in range(0, len(n)):
        ne = int(input('Valor inválido.Por favor escolha um número de 0 à 20: '))
    print(f'{ne} escrito por extenso: ')
    print(n[ne])
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in ('S', 'N'):
        continuar = str(input('Valor inválido,tente novamente.Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break
