vc = int(input('Velocidade do carro: '))
vp = int(80)
m = float((vc - 80) * 7.00)
if vc > vp:
    str(print('''Você ultrapassou o limite de velicidade permitido.
Você foi multado em: R$ {:.2f}
Sua velocidade: {} Km/h
Limite permitido:{} Km/h'''.format(m, vc, vp)))
else:
    ''