n = int(input('Digite o numero a ser convertido: '))
opcao = int(input('Escolha a base da Conversão: \n1 - Para Binário \n2 - Para Octal \n3 - Para Hexadeximal \n'))

binario = format(n, "b")
octal = format(n, "o")
hexa = format(n, "x")

if opcao == 1:
    print ('O numero {} convertido para binario é {}'.format(n, binario))
elif opcao == 2:
    print('O numero {} convertido para Octal é {}'.format(n, octal))
elif opcao == 3:
    print('O numero {} convertido para Hexadecimal é {}'.format(n, hexa))
print('---FIM---')
