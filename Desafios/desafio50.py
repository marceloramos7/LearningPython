soma=0
for c in range(1, 7):
    n = int(input('Digite o valor do {} número: '.format(c+1)))
    num=n%2
    if num==0:
        soma=soma+n
    else:
        print('Este número {} não é par'.format(n))
print('A soma dos valores pares é {}'.format(soma))

