n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1<n2:
    print('O maior valor é {} o menor é {}.'.format(n2, n1))
elif n2<n1:
    print('O maior valor é {} o menor é {}.'.format(n1, n2))
elif n2 == n1:
    print('Os valores {} e {} são iguais.'.format(n1, n2))
print('---FIM---')
