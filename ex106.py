cor = {'azul': '\033[7;40;34m', 'verde': '\033[7;49;32m', 'default': '\033[m'}
def msgf(msg):
    '''
    Função para formatar titulos ou mensagens.
    :param msg: uma mensagem/titulo.
    :return: a mensagem formatada com cor de fundo escolhida.
    '''
    f = f"{4 * '-'}{len(msg) * '-'}{4 * '-'}"
    return f'{f}\n{4 * " "}{msg}\n{f}'


while True:
    print(f"{cor['azul']}{msgf('Interactive Help Python')}")
    foub = str(input(f'{cor["default"]}Digite uma função ou biblioteca: {cor["verde"]}')).strip()
    help(foub)
    if foub.lower() == 'fim':
        break
