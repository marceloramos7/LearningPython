valores=[]
pares=[]
impares=[]
count=0

for c in range(0, 7):
    valores.append(int(input('Digite um Valor: ')))

    if valores[c] % 2 == 0:
        pares.append(valores[c])
    else:
        impares.append(valores[c])

    #valores.clear()
valores.clear()
valores.append(pares[:])
valores.append(impares[:])
print(valores)
print(f'Os números digitados foram {valores}')
print(f'Os números pares são {pares}')
print(f'Os números ímpares são {impares}')

