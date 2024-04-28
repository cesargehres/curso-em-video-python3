print('Sequência de Fibonacci')
n = 1
count = 2
inte = False
t1 = 0
t2 = 1
t3 = 0
while n != 0:
    if inte == False:
        n = int(input('Quantos termos você quer mostrar? '))
        inte = True
    elif inte == True:
        count = count - count
        n = int(input('\nQuantos termos mais você quer mostrar? '))
    while count < n:
        count += 1
        if t3 == 0:
            print('{} -> '.format(t3), end='')
            t3 = t2 + t1
            print('{} -> {} -> '.format(t3, t3), end='')
        elif t3 > 0:
            t1 = t2
            t2 = t3
            t3 = t2 + t1
            print('{} -> '.format(t3), end='')
print('Fim', end='')
