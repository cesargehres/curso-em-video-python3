def voto(ano):
    """
    Situação de voto
    :param ano: Ano de nascimento
    :return:Situação de voto, se é preciso votar ou não
    """
    from datetime import date
    idade = date.today().year - ano
    if 16 <= idade <= 18 or idade >= 65:
        return f'{idade} anos: VOTO OPCIONAL'
    elif 18 <= idade <= 65:
        return f'{idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'{idade} anos: NÃO VOTA'


#Programa Principal
nascimento = int(input('Digite o ano de nascimento: '))
print(voto(nascimento))
