

def resumo(n, a=10, d=10):
    na = aumentar(n, pc=a)
    nd = diminuir(n, pc=d)
    ndo = dobro(n)
    nme = metade(n)
    return f'{30 * "-="}\n' \
           f'{25 * " "}RESUMO\n' \
           f'{30 * "-="}\n' \
           f'R$ {n} com aumento de {a}% {na:>30}\n' \
           f'R$ {n} com redução de {d}% {nd:>30}\n' \
           f'Dobro de R$ {n} {ndo:>40}\n' \
           f'Metade de R$ {n} {nme:>39}'
