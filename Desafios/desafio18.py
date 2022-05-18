import math

angulo = float(input('Digite o ângulo que vc deseja: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O valor do seno é {:.2f} do cosseno é {:.2f} e da tangente é {:.2f}'.format(seno, cos, tan))