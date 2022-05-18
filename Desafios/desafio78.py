valores=[]

for count in range (0, 5):
    valores.append(int(input(f'Digite o {count+1}º valor da lista: ')))

print(valores)
print(f'O maior valor da Lista é {max(valores)}, e o menor é {min(valores)}')





