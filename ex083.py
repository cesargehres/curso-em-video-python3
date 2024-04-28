pa = []
pf = []
correto = True
exp = str(input('Digite sua expressão: '))
for i, v in enumerate(exp):
    if '(' in v:
        pa.append(i)
    if ')' in v:
        pf.append(i)
        if len(pf) > len(pa):
            correto = False
            break
if len(pa) != len(pf):
    correto = False
if correto == True:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')
