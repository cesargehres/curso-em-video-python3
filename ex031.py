v = float(input('Qual a distancia a ser percorrida?: '))
if v <= 200:
    print('A viagem irá custar: R$ {:.2f}'.format((v * 0.50)))
else:
    print('A viagem irá custar: R$ {:.2f}'.format(v * 0.45))