from random import randint
T = 2
print('-------------- {} --------------'.format(T + 1))
print('Vou pensar em um número de 1 à 10.')
print('Ainda restam {} tentativas'.format(T + 1))
NE = randint(1,10)
NR = int(input('Em que número estou pensando?'))
while NR != NE and T != 1:
    T -= 1
    print('-------------- {} --------------'.format(T + 1))
    NR = int(input('Você errou,ainda restam {} tentativas...Qual número estou pensando?'.format(T + 1)))
if T == 1 and NE <= 5 :
    print('------------- Dica -------------')
    print('Como você esta passando vergonha,vou dar uma dica')
    print('O número é menor que 6')
    NR = int(input('É sua última tentativa:'))
elif T == 1 and NE >= 5 :
    print('------------- Dica -------------')
    print('Como você esta passando vergonha,vou dar uma dica')
    print('O número é maior que 4')
    NR = int(input('É sua última tentativa:'))
if NR == NE:
    print('------------- Wins -------------')
    print('Você acertou,o número que eu estava pensando era {},você respondeu {}.'.format(NE, NR))
elif NR != NE:
    print('---------- Game Over -----------')
    print('Você perdeu kkkkjj\n'
         'O número que estava pensando era {},e você respondeu {}'.format(NE, NR))
