from collections import OrderedDict
valores=[]
while True:
    valores.append(int(input('Digite um Valor: ')))
    escolha = input('Quer continuar [S/N]? ').upper().strip()[0]

    if escolha=='N':
        print('Saiu')
        break
valoresfinal = list(OrderedDict.fromkeys(valores))
valoresfinal.sort()
print(valoresfinal)