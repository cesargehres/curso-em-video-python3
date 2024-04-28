import moeda

n = float(input('Digite um valor: R$ ').replace(',', '.'))
print(f'{moeda.moeda(n)} com aumento de 10%: {moeda.aumentar(n, 10)}')
print(f'{moeda.moeda(n)} com redução de 10%: {moeda.diminuir(n, 10)}')
print(f'Dobro de {moeda.moeda(n)}: {moeda.dobro(n)}')
print(f'Metade de {moeda.moeda(n)}: {moeda.metade(n)}')
