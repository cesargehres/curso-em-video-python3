c = 0
Lista = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar',
         'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')
while True:
    print(f'''{f'As vogais de {Lista[c].upper()} são:':35}''' if c == 0
          else f'''\n\n{f'As vogais de {Lista[c].upper()} são:':35}''', end=' ')
    if 'A' in Lista[c].upper():
        print('A', end=' ')
    if 'E' in Lista[c].upper():
        print('E', end=' ')
    if 'I' in Lista[c].upper():
        print('I', end=' ')
    if 'O' in Lista[c].upper():
        print('O', end=' ')
    if 'U' in Lista[c].upper():
        print('U', end=' ')
    c += 1
    if c == len(Lista):
        break
