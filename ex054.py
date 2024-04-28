from datetime import date
m = 0
ano = date.today().year
for c in range(1, 8):
    p = int(input('Digite o ana de nascimento da pessoa {}: '.format(c)))
    idade = ano - p
    if idade >= 18:
        m += 1
print('Das {} pessoas, {} são maiores de idade e {} são menores de idade.'.format(c, m, c - m))
