idade=0
count=0
homem=0
mulher=0
adulto=0
menormulher=0
menorhomem=0

while True:
    print('=-=' * 15)
    print('CADASTRO DE PESSOAS')
    print('=-=' * 15)

    idade=int(input('Idade: '))
    sexo=input('Sexo [M/F]: ').upper().strip()[0]
    escolha=input('Deseja continuar [S/N]: ').upper().strip()[0]
    count+=1
    idade=idade+0

    if sexo=='M':
        homem+=1
        if idade>=18:
            adulto+=1
        else:
            menorhomem+=1

    if sexo=='F':
        mulher += 1
        if idade>=18:
            adulto+=1
        else:
            menormulher+=1

    if escolha =='N':
        media=idade/count
        break

print(f'Total de pessoas com mais de 18 anos {adulto}')
print(f'Pessoas do sexo masculino {homem}')
print(f'Pessoas do sexo feminino {mulher}')
print(f'Menor de idade mulheres {menormulher} e homeNS {menorhomem}')
print(f'A média de idade dos cadastrados é {media}')
