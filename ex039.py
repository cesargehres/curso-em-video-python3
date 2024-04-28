from datetime import date
sexo = int(input('''Qual o seu sexo?
\033[35m1\033[m para Masculino
\033[35m2\033[m para Feminino
'''))
if sexo == 2:
    print('Você é mulher e não precisa se alistar')
elif sexo == 1:
    an = int(input('Digite seu ano de nascimento: '))
    data = date.today().year
    idade = data - an
    if idade == 18:
        print('Quem nasceu em {} tem {} anos.'.format(an, idade))
        print('Deve se alistar esse ano.')
    elif idade > 18:
        print('Quem nasceu em {} tem {} anos.'.format(an, idade))
        print('Deveria ter se alistado há {} anos, em {}'.format(idade - 18, an + 18))
    elif idade < 18:
        print('Quem nasceu em {} tem {} anos.'.format(an, idade))
        print('Deverá se alistar em {},ainda faltam {} anos.'.format(an + 18, 18 - idade))
else:
    print('Valor inválido!')
