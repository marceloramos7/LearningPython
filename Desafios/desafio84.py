dados=[]
pessoas=[]
count=pesomaior=pesomenor=0
pesadas=leves=[]

while True:
    dados.append(str(input('Digite o nome: ')).capitalize())
    dados.append(int(input('Digite o peso em KG: ')))
    pessoas.append(dados[:])
    dados.clear()
    escolha = input('Quer continuar [S/N]? ').upper().strip()[0]
    count+=1

    for p in pessoas:
        if count==1:
            pesomaior=p[1]
            pesomenor=p[1]

        if pesomaior<=p[1]:
            pesomaior=p[1]
            pesadas=p[0]

        if pesomenor>p[1]:
            pesomenor=p[1]
            leves=p[0]

    if escolha=='N':
        break

print(f'Foram cadastradas {count} pessoas.')
print(f'A pessoa mais pesada é {pesadas} pesa {pesomaior}Kg')
print(f'A pessoa mais leve é {leves} pesa {pesomenor}Kg')
