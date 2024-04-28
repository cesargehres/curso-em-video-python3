sexo = input(str('Informe seu sexo: [M/F]')).strip()
while sexo not in 'MmFf':
    sexo = input(str('Valor inválido,digite seu sexo: [M/F]')).strip()
print(str('Sexo registrado com sucesso.'))
