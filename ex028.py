import random
print('\033[07m><\033[m' * 25)
print('>>> Tente adivinhar o numero de 1 até 5. <<<')
print('\033[07m><\033[m' * 25)
ne = int(input('Escolha um número: '))
ns = random.randint(1, 5)
print('O número sorteado era {},você escolheu {}.'.format(ns, ne))
if ne == ns:
    print('\033[32mParabéns,você ganhou!\033[m')
else:
    print('\033[31mVocê perdeu,tente de novo!\033[m')
