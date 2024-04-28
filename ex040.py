vermelho = '\033[31m'
branco = '\033[m'
verde = '\033[32m'
amarelo = '\033[33m'
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2) / 2
if media > 7:
    print('Média {}{:.1f}{}, aluno {}APROVADO{}!'.format(verde, media, branco, verde, branco))
elif media >= 5 and media <= 6.9:
    print('Média {}{:.1f}{}, aluno de {}RECUPERAÇÃO{}!'.format(amarelo, media, branco, amarelo, branco))
elif media < 5:
    print('Média {}{:.1f}{}, aluno {}REPROVADO{}!'.format(vermelho, media, branco, vermelho, branco))
