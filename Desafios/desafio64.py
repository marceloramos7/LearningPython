n=0
n1=0
while n != 999:
    n = int(input('Digite um número [999 para PARAR]: '))
    if n != 999:
        n1 = n1 + n
        #print('A soma dos valores é {}'.format(n1))
print('A soma dos valores é {}'.format(n1))
print('FIM')