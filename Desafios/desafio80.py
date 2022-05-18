lista=[]
for count in range(0, 5):
    valor=int(input('Digite um valor: '))
    if count==0 or valor > lista[-1]:
        lista.append(valor)
    else:
        pos=0
        while pos < len(lista):  #Vai do 0 até a última posição
            if valor<=lista[pos]:    #Vai verificar se o número em cada posição ou menor ou igual a ele
                lista.insert(pos, valor)
                print(f'O valor foi adicionado na posição {pos}')
                break
            pos+=1
print(f'Os valores digitado em ordem foram {lista}')