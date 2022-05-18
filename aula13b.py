i = int(input('Entre com Inicio: '))
f = int(input('Entre com Final: '))
p = int(input('Entre com o Intervalo: '))

for c in range(i, f, p):
    print('Inicio:{} \nFIM:{} \nIntervalo:{} \nCont:{} \n---------------'.format(i, f, p, c))
print('__FIM__')
