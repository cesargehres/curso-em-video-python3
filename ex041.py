from datetime import date
verde = '\033[32m'
branco = '\033[m'
an = int(input('Qual o ano de nascimento?'))
idade = date.today().year - an
print('O atleta que nasceu em {}, tem {} anos'.format(an, idade))
if idade <= 9:
    print('e é um(a) atleta {}MIRIM{}.'.format(verde, branco))
elif 9 < idade <= 14:
    print('e é um(a) atleta {}INFANTIL{}.'.format(verde, branco))
elif 14 < idade <= 19:
    print ('e é um atleta {}JÚNIOR{}.'.format(verde, branco))
elif 19 < idade <= 25:
    print('e é um atleta {}SÊNIOR{}.'.format(verde, branco))
elif idade > 25:
    print('e é um atleta {}MASTER{}.'.format(verde, branco))
