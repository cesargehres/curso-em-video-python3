n = int(input('Digite um número: '))
c = str(input('Quer continuar?[S/N] ')).strip().upper()
r = True
count = 1
s = m = 0
nm = NM = 0
while r == True:
    if n < nm:
        nm = n
    elif n > NM:
        NM = n
    if c == 'N':
        r = False
    elif c == 'S':
        n = int(input('Digite um número: '))
        c = str(input('Quer continuar?[S/N] ')).strip().upper()
        s += n
        r = True
        count += 1
m = s / count
print('Você digitou {} números,a média deles é de {}.\n'
      'O número maior é {}.\n'
      'E o número menor é {}.'.format(count, m, NM, nm))
