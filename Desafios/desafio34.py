salario = float(input('Qual o valor do salario do funcionario? '))

if salario<=1250:
    novo = salario + (salario*15/100)
else:
    novo = salario + (salario*10/100)
print('\033[4;34;42mQuem recebia {} passa a receber {}'.format(salario,novo))
