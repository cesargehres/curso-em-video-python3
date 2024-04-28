def aumentar(n=0, pc=10, fm=True, moeda='R$'):
    res = n + (n * pc / 100)
    if fm != False:
        form = f'{moeda} {res:.2f}'.replace('.', ',')
        return form
    else:
        return res


def diminuir(n=0, pc=10, moeda='R$'):
    res = n - (n * pc / 100)
    if moeda != False:
        form = f'{moeda} {res:.2f}'.replace('.', ',')
        return form
    else:
        return res


def dobro(n=0, moeda='R$'):
    res = n * 2
    if moeda != False:
        form = f'{moeda} {res:.2f}'.replace('.', ',')
        return form
    else:
        return res


def metade(n=0, moeda='R$'):
    res = n / 2
    if moeda != False:
        form = f'{moeda} {res:.2f}'.replace('.', ',')
        return form
    else:
        return res


def moedaf(n=0, moeda='R$'):
    form = f'{moeda} {n:.2f}'.replace('.', ',')
    return form


def resumo(n, a=10, d=10):
    na = aumentar(n, pc=a)
    nd = diminuir(n, pc=d)
    ndo = dobro(n)
    nme = metade(n)
    return f'{30 * "-="}\n' \
           f'{25 * " "}RESUMO\n' \
           f'{30 * "-="}\n' \
           f'{f"Valor Inicial:":50} {moedaf(n)}\n' \
           f'{f"Aumento de {a}%:":50} {na}\n' \
           f'{f"Redução de {d}%:":50} {nd}\n' \
           f'{f"Dobro:":50} {ndo}\n' \
           f'{f"Metade:":50} {nme}'
