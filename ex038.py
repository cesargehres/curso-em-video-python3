n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O número {}{}{} é maior.'.format('\033[4;33m', n1, '\033[m'))
elif n2 > n1:
    print('O número {}{}{} é maior.'.format('\033[4;33m', n2, '\033[m'))
else:
    print('Os dois números tem o mesmo valor.')
