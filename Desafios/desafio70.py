preco=0
total=0
barato=''
count=0
precobarato=0

print('=-=' * 15)
print('MERCADÃO MR7')
print('=-=' * 15)

while True:

    produto=input('Produto: ').strip()
    count+=1

    preco=float(input('Preço: '))
    total+=preco

    escolha=input('Quer continuar [S/N]? ').upper().strip()[0]

    if count==1:
        barato=produto
        precobarato = preco

    else:
        if preco<precobarato:
            barato=produto

    if escolha=='N':
        print(f'O quantidade de produtos foi {count}')
        print(f'O valor total da compra é de R${total}')
        print(f'O produto mas barato é {barato}')
        break

print('=-=' * 15)
print('FIM DA COMPRA')
print('=-=' * 15)