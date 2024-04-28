MM = PPB = rep = Total = 0  #MM = Produtos que são > 1000 e/PPB = Preço do Produto Mais Barato/rep = Primeira repetição/Total = Preço Total
NPB = ''   #NPB = Nome do produto mais barato
while True:
    Nome = str(input('Nome do produto: ')).strip().title()
    Preco = float(input('Preço do produto: R$ '))
    Total += Preco
    if rep == 0:
        NPB = Nome
        PPB = Preco
        Total = Preco
        rep = 1
    else:
        if Preco < PPB:
            NPB = Nome
            PPB = Preco
    if Preco > 1000:
        MM += 1
    continuar = str(input('Quer continuar?[S/N] ')).strip().upper()
    while continuar not in ('S', 'N'):
        continuar = str(input('Por favor digite uma opção válida [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'Total = R$ {Total:.2f}')
print(f'{MM} Produto(s) Custou(Custaram) mais de R$ 1000.00')
print(f'O produto mais barato foi {NPB} que custo R$ {PPB:.2f}')
