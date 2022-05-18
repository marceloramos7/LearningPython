n1 = int(input('Digite o preimeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

#verificando o menor valor
if n1<n2 and n1<n3:
    print('O menor numero é {}'.format(n1))
if n2<n1 and n2<n3:
    print('O menor numero é {}'.format(n2))
if n3<n1 and n3<n2:
    print('O menor numero é {}'.format(n3))
#verificando o maior valor
if n1>n2 and n1>n3:
    print('O maior numero é {}'.format(n1))
if n2>n1 and n2>n3:
    print('O maior numero é {}'.format(n2))
if n3>n1 and n3>n2:
    print('O maior numero é {}'.format(n3))

print('---Fim---')