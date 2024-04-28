n = str(input('Digite o seu nome completo:')).strip()
print('Nome completo:{}'.format(n))
print('Primeiro nome:{}'.format(n.split()[0]))
print('Último nome:{}'.format(n.split()[-1]))
