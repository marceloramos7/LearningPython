print('PROGRAMA DE RECONHECIMENTO DE NÚMEROS')
print('=-='*13)
numeros = ('ZERO', 'UM', 'DOIS' , 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ')
n = int(input('Escolha um número de 1 a 10: '))

if 0<=n<=10:
    print(f'Vc digitou o número {numeros[n]}')
else:
    print('VALOR INCORRETO')
print('FIM')