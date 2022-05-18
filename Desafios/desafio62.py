print('Gerador de PA')
print('=-='*10)

primeiro = int(input("Primeiro elemento: ") )
razao = int(input("Razao da PA: ") )
termo = primeiro
count = 1
total=0
mais=10

while mais!=0:
    total=total+mais
    while count<=total:
        print('{} -> '.format(termo), end='')
        termo+=razao
        count+=1

    print('PAUSE')
    mais = int(input('Quantos termos mais vc quer mostrar? '))
print('FIM')
