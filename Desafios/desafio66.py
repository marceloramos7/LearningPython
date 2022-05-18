n=0
soma=0
while True:
    n = int(input('Digite um número [999 para PARAR]: '))
    if n == 999:
        break
    soma+=n
print(f'A soma dos valores é {soma}')
print('FIM')