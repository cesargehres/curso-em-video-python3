import datetime

Trabalhador = {'Nome': str(input('Nome: ')).strip().title(),
               'Idade': datetime.date.today().year - int(input('Ano de Nascimento: ')),
               'CTPS': int(input('Carteira de Trabalho : [0 se não tiver]'))}
if Trabalhador['CTPS'] != int(0):
    Trabalhador['Contratação'] = int(input('Ano de Contratação: '))
    Trabalhador['Salário'] = float(input('Salário: R$ '))
    Trabalhador['Aposentadoria'] = (35 + Trabalhador['Idade']) - (datetime.date.today().year - Trabalhador['Contratação'])
else:
    Trabalhador['CTPS'] = str('Inexistente')

print('-=' * 40)
for k, v in Trabalhador.items():
    if k in 'Salário':
        print(f'{k}: R$ {v:.2f}')
    elif k in 'Aposentadoria':
        print(f'{k}: com {v} anos')
    else:
        print(f'{k}: {v}')
