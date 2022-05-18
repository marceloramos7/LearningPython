lanche=['Ham', 'Suco', 'Pizza', 'Bolo', 'Batata', 'Pudim', 'Brigadeiro']

del lanche[1]   #Apagar
print(lanche)

lanche.pop(3)   #Normalmente usado pra apagar o ultimo Indice, mas pode apagar qualquer
print(lanche)

lanche.pop()    #Apaga o ultimo
print(lanche)

lanche.remove('Pizza')  #######Apaga pelo conteúdo########
print(lanche)

if 'Pizza' in lanche:       #Só vai remover se estiver na Lista
    lanche.remove('Pizza')
else:
    print('Nao tem Pizza')
    
lanche.sort()
print(lanche)