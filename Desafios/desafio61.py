print('Gerador de PA')
print('=-='*10)

primeiro = int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") )
termo = primeiro
count = 1

while count<=10:
    print('{} -> '.format(termo), end='')
    termo+=razao
    count+=1

print('FIM')
