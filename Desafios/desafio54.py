for c in range(0, 7):
    ano=int(input('Qual o seu ano de nascimento? '))
    idade=2022-ano
    if idade>=21:
        print('Vc tem {} anos, vc é maior de idade.'.format(idade))
    else:
        print('Vc tem {} anos, é menor de idade.'.format(idade))
print('FIM')
