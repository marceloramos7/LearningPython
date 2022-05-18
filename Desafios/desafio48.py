soma=0
for c in range(1,501,2):
    n = c%3
    if n==0:
        #print('O numero {} é multiplo de 3.'.format(c))
        soma=soma+c
print('A soma dos numeros multiplos de 3,\nentre é 1 e 500 é: {}'.format(soma))
