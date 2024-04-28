Nome = str(input('Digigte seu nome completo:')).strip()
NOME = Nome.upper()
nome = Nome.lower()
ns = Nome.split()
nse = ''.join(ns)
nsen= len(nse)
qcpn = len(ns[0])
print('''Nome com letras maiúsculas:{}
Nome com letras minúsculas:{}
Números de letras que há no nome:{}
Número de letras que há no primeiro nome:{}.'''.format(NOME, nome, nsen, qcpn))
