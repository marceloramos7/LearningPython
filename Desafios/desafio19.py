from random import choice

n1 = str(input('Entre com o primeiro nome: '))
n2 = str(input('Entre com o segundo nome: '))
n3 = str(input('Entre com o terceiro nome: '))
n4 = str(input('Entre com o quarto nome: '))

nomes = [n1 ,n2, n3, n4]
sorteio = choice(nomes)

print('O nome sorteado é {}'.format(sorteio))
