import math

co = float(input('Entre com o valor do cateto oposto: '))
ca = float(input('Entre com o valor do cateto adjacente: '))
hi = math.hypot(co, ca)

print('A hipotenusa é igual a {}'.format(hi))