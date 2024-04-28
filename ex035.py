m1 = float(input('Medida 1: '))
m2 = float(input('Medida 2: '))
m3 = float(input('Medida 3: '))
if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
    print('\033[32mEssas medidas podem formar um triângulo.\033[m')
else:
    print('\033[31mEssas medidas não podem formar um triângulo.\033[m')
