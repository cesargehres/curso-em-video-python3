l = []
count = dig5 = 0
while True:
    n = int(input('Digite um número: '))
    if n == 5:
        dig5 += 1
    l.append(n)
    count += 1
    con = ''
    lr = l[:]
    while con not in ('S', 's', 'N', 'n'):
        con = str(input('Quer continuar?(S/N) '))
        if con in ('S', 's'):
            break
    if con in ('N', 'n'):
        break
lr.sort(reverse=True)
print(f'''Foram digitados {count} números.
A lista de números em forma decrescente é: {lr}''')
if dig5 > 0:
    print(f'O número 5 foi digitado {dig5} vezes e esta localizado nas posições:', end=' ')
    ci = 0
    while ci != len(l):
        if l[ci] == 5:
            print(f'{ci}', end=' ')
        ci += 1
else:
    print('O número 5 não foi digitado nenhuma vez.')
