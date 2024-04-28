frase = str(input('Escreva uma frase: ')).strip().upper()
frase1 = frase.replace(' ', '')
frase2 = frase1[::-1]
if frase1 == frase2:
    print('{} é um PALÍNDROMO.\n{}\n{}'.format(frase, frase1, frase2))
else:
    print('{} nao é um PALÍNDROMO.\n{}\n{}'.format(frase, frase1, frase2))
