da = float(input('Dias alugados:'))
kr = float(input('Km rodados:'))
tp = da * 60.00 + kr * 0.15
print('Total a pagar:R${:.2f}'.format(tp))
