dist = float(input('Qual a distância da viagem? '))

if dist<200:
    v1 = float(dist * 0.5)
    print('O valor da sua passagem é de R${:.2f}'.format(v1))
else:
    v2 = float(dist*0.45)
    print('O valor da sua passagem é de R${:.2f}'.format(v2))