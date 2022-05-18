sexo = '1'
while sexo != 'M' or sexo != 'F':
    sexo = input('Qual seu sexo [M/F]? ').upper()
    if sexo in 'M F':
        print('Salvo com Sucesso!')
        sexo=sexo
    else:
        sexo = '1'
print('--FIM--')
