nome = input('Bom dia, qual seu nome? ')
altura = float(input('{} qual a sua altura? '.format(nome)))
peso = float(input('Qual o seu peso? '))

imc = peso/(altura*altura)

if imc<18.5:
    print('{} vc está abaixo do peso '.format(nome))
elif imc>=18.5 and imc<=25:
    print('{} vc está no peso ideal'.format(nome))
elif imc>25 and imc<=30:
    print('{} vc está em sobrepeso'.format(nome))
elif imc>30 and imc<=40:
    print('{} vc está obeso'.format(nome))
elif imc>40:
    print('{} cuide se, vc está em obesidade morbida'.format(nome))

