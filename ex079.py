n = []
while True:
    n1 = (int(input('Digite um número: ')))
    n.append(n1)
    nr = n.count(n1)
    if nr > 1:
        n.pop()
    continuar = str(input('Quer continuar?(S/N) '))
    while continuar not in ('S', 's', 'N', 'n'):
        continuar = str(input('Valor inválido,Digite (S) para continuar ou (N) para parar: '))
    if continuar in ('N', 'n'):
        break
print(f'Os números digitados foram:', end=' ')
for l, v in enumerate(sorted(n)):
    print(f'{v}, ' if l + 1 < len(n) else f'{v}', end='')
