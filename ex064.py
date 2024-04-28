np = count = nc = ns1 = ns2 = 0
while np < 999:
    ns1 = np
    ns2 += ns1
    np = int(input('Digite um número [999 para parar]: '))
    nc = count
    count += 1
print('Você digitou {} números e a soma entre eles é {}.'.format(nc, ns2))
