def notas(*nt, sit=False):
    '''
    Função para analisar as notas de um aluno.
    :param nt: uma ou mais notas dos alunos(aceita várias).
    :param sit: parametro opcional,indicando se deve ou não indicar adicionar a situação do aluno.
    :return: dicionário com várias informações da situação da turma
    '''
    notas = dict()
    m = sum(nt) / len(nt)
    notas['Total'] = len(nt)
    notas['Maior nota'] = max(nt)
    notas['Menor nota'] = min(nt)
    notas['Média'] = m
    if sit:
        if m >= 7:
            notas['Situação'] = 'Boa'
        elif m < 7 and m >= 6:
            notas['Situação'] = 'Regular'
        else:
            notas['Situação'] = 'Ruim'
    return notas


resp = notas(7, 10, 3, 8, sit=True)
print(resp)
