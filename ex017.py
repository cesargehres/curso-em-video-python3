from math import pow
a = float(input('Digite o cateto oposto:'))
b = float(input('Digite o cateto  adjacente:'))
print('Hipotenusa:{:.2f}'.format(((pow(a, 2) + pow(b, 2))**(1/2))))
