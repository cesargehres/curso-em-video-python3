def fatorial(num=0, show=False):
    """
    Caculadora de fatorial
    :param num: int(número)
    :param show: mostrar soma do fatorial
    :return: fatorial
    """
    s = num
    for c in range(num, 0, -1):
        if c < num:
            s *= c
        if show == True:
            print(f'{c} x 'if c > 1 else f'{c} = ', end='')
    return s


#Programa principal
num = int(input('Digite um número para calcular seu fatorial: '))
print(fatorial(num))
