s = float(input('Salário: R$'))
if s <= 1250.00:
    print('Aumento de R${:.2f}'.format(s / 100 * 15 + s))
else:
    print('Aumento de R${:.2f}'.format(s / 100 * 10 + s))
