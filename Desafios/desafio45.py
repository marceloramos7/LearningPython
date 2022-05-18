from random import choice
nome = input('Bom dia, qual seu nome? ')
print('{} vamos jogar jokenpô!!'.format(nome))

lista = ['Pedra', 'Papel', 'Tesoura']
lista = choice(lista)

escolha = input('Escolha Pedra, Papel ou Tesoura: \n:>')

if escolha==lista:
    print('EMPATE ambos escolheram {}'.format(lista))
elif escolha=='Pedra' and lista=='Papel':
    print('EU VENCI, eu escolhi {} e vc {}'.format(lista,escolha))
elif escolha=='Pedra' and lista=='Tesoura':
    print('VC VENCEU, eu escolhi {} e vc {}'.format(lista, escolha))
elif escolha=='Papel' and lista=='Pedra':
    print('VC VENCEU, eu escolhi {} e vc {}'.format(lista, escolha))
elif escolha=='Papel' and lista=='Tesoura':
    print('EU VENCI, eu escolhi {} e vc {}'.format(lista, escolha))
elif escolha=='Tesoura' and lista=='Papel':
    print('VC VENCEU, eu escolhi {} e vc {}'.format(lista, escolha))
elif escolha=='Tesoura' and lista=='Pedra':
    print('EU VENCI, eu escolhi {} e vc {}'.format(lista, escolha))
print('--FIM DE JOGO--')
