l = []
while True:
    n = (input('Digite um número (ou "P" para parar): '))
    if n in ('P', 'p'):
        break
    else:
        l.append(int(n))
l.sort()
lp = []
li = []
c = 0
while c < len(l):
    if l[c] % 2 == 0:
        lp.append(l[c])
    else:
        li.append(l[c])
    c += 1
print(f'Números digitados: {l}')
print(f'Números pares digitados: {lp}')
print(f'Números impares digitados: {li}')
