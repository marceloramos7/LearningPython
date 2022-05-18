n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))
m = (n1+n2)/2
print('A sua média foi {:.2f}'.format(m))
if m<=5.9:
    print('Vc foi reprovado. ')
else:
    print('Parabéns, vc foi aprovado.')
print('Fim')