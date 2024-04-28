print('\033[1;34mCorversor de números\033[m')
n = int(input('\033[;34mDigite um número:\033[m'))
print('\033[34mAgora esolha a conversão: \033[m')
print('''\033[35m1 \033[mpara \033[36mbinário\033[m
\033[35m2 \033[mpara \033[36m octal\033[m
\033[35m3 \033[mpara \033[36m hexadecimal\033[m''')
c = int(input(''))
if c == 1:
    print('{} em binário é {}.'.format(n, bin(n)[2:]))
elif c == 2:
    print('{} em octal é {}.'.format(n, oct(n)[2:]))
elif c == 3:
    print('{} em hexadecimal é {}.'.format(n, hex(n)[2:]))
