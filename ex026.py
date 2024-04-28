p = str(input('Digite uma frase:')).strip()
q = p.lower().count('a')
i = p.lower().find('a')+1
f = p.lower().rfind('a')+1
print('''Em {} existe(m):
{} A(s)
Que começa(m) na posição:{}
E termina(m) na posição:{}'''.format(p, q, i, f))
