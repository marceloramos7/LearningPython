nome = input('Qual o seu nome completo? ').strip()
nome = nome.split()

print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))
