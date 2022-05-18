valores=[]
while True:
    valores.append(int(input('Digite um Valor: ')))
    escolha = input('Quer continuar [S/N]? ').upper().strip()[0]

    if escolha=='N':
        print('Saiu')
        break

print(f'Foram digitados {len(valores)} números.')
valores.sort()
print(f'Ordem crescente {valores}')

if 5 in valores:
     print(f'o número 5 esta na {valores.index(5)+1}º posição')
else:
     print('Vc não digitou o número 5.')
