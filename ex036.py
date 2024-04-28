vc = float(input('\033[33mValor da casa: R$ \033[m'))
sc = float(input('\033[33mSalário do comprador: R$\033[m'))
ap = float(input('\033[33mAnos para pagar a casa:\033[m'))
pm = vc / ap / 12
s = sc / 100 * 30
if pm <= s:
    print(str('\033[32mSeu financiamento foi aceito!\033[m'))
else:
    print(str('\033[31mDesculpe, seu financiamento foi negado!\033[m'))