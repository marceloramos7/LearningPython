n=1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n!=0:        #Aqui ele nao contara o Zero como um numero
        if n%2 ==0:
            par+=1
        else:
            impar+=impar
print('Vc digitou {} numeros pare e {} impares'.format(par, impar))