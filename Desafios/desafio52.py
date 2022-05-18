n = int(input("Verificar numeros primos ate: "))
mult=0
for count in range(2,n):
    if (n % count == 0):
        print("Não é primo. Múltiplo de {}".format(count))
        mult += 1
if(mult==0):
    print("É primo")

