sexo = input('Qual seu sexo \nEscolha M ou F: ').upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input('Dados Inválidos. Qual seu sexo \nEscolha M ou F: ').upper().strip()[0]
print('Sexo {} registrado com sucesso. '.format(sexo))

