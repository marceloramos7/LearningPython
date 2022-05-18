'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

escolha='S'
count = n1 = maior =0
while escolha in 'S s':
    n = int(input('Digite um número: '))
    n1=n1+n
    count += 1
    maior=n
    escolha=input('Quer continuar [S/N]: ').upper().strip()[0]
    if n>maior:
        maior=n
#if escolha=='n' or escolha=='N':
media=n1/count
print('O maior número é {}'.format(maior))
print(f'O maior número é {maior}')
print('FORMAT Vc digitou {} números e a média foi de {:.2f}'.format(count, media))
print(f'Vc digitou {count} números e a média foi de {media:.2f}')
