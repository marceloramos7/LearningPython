valores = []

for cout in range(0, 5):
    valores.append(int(input('Digite um valor da lista: ')))

for i, v in enumerate(valores):
    print(f'O {v} está no indice {i}')
print('FIM DA LISTA')
