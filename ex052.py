n = int(input('Digite um número: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        total += 1
if total == 2:
    print('{} é primo'.format(n))
else:
    print('{} não é primo'.format(n))
