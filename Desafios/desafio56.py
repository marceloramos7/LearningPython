'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre: a média de idade do grupo,
 qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

somaidade=0
mediaidade=0
velhohomem=0
nomevelho=''
countmulher=0

for pessoa in range(1, 5):
    print('----{}ª PESSOA----'.format(pessoa))
    nome = input('Qual o nome da {}ª pessoa? '.format(pessoa)).strip()
    idade = int(input('{} qual a sua idade? '.format(nome)))
    sexo = input('Qual seu sexo? [M/F] ')
    somaidade += idade
    if pessoa==1 and sexo in ('Mm Masculino masculino'):
        nomevelho=nome
        velhohomem=idade

    if sexo in ('Mm') and idade >velhohomem:
        velhohomem=idade
        nomevelho=nome

    if sexo in ('Ff') and idade<20:
        countmulher+=1

mediaidade=somaidade/4
print('A média de idade das 4 pessoas é {} anos'.format(mediaidade))
print('É {} a pessoa mais velha e tem {} anos.'.format(nomevelho, velhohomem))
print('Tem {} mulheres com menos de 20 anos'.format(countmulher))