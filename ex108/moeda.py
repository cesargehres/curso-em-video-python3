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


def moedaf(valor=0, moeda='R$'):
    form = f'{moeda} {valor:.2f}'.replace('.', ',')
    return form
