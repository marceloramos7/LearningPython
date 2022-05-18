escolha=0
while escolha != 5:
    n1 = float(input('Entre com o primeiro valor: '))
    n2 = float(input('Entre com o segundo valor: '))
    escolha = int(input('Escolha uma das opçoes para executar \n1-Somar \n2-Multiplicar \n3-Maior \n4-Novos Números \n5-Sair \n'))

    if escolha==1:
        print('A soma dos valores é {}'.format(n1+n2))
        escolha=5

    if escolha==2:
        print('A multiplicação dos valores é {}'.format(n1*n2))
        escolha=5

    if escolha==3:
        if n1>n2:
            print('O maior número é {}'.format(n1))
            escolha=5
        if n2>n1:
            print('O maior valor é {}'.format(n2))
            escolha=5
        else:
            print('Os valaores são iguais.')
            escolha=5

    if escolha==4:
        escolha=4

    if escolha==5:
        print('Saiu')

