count=0
while True:
    n=int(input('Tabuada de qual valor? '))
    if n >= 0:
        for count in range (1, 11):
            print(f'{n} x {count} = {n*count}')
    else:
        print('FIM DA TABUADA')
        break
    print('=-='*10)
