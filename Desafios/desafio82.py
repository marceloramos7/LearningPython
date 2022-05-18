valores=[]
pares=[]
impares=[]
count=0
while True:
    valores.append(int(input('Digite um Valor: ')))
    escolha = input('Quer continuar [S/N]? ').upper().strip()[0]

    if escolha=='N':
        print('Saiu')
        break

for c in valores:
    if c % 2 == 0:
        pares.append(c)
        count += 1
    else:
        impares.append(c)
        count += 1

print(f'Os números digitados foram {valores}')
print(f'Os números pares são {pares}')
print(f'Os números ímpares são {impares}')