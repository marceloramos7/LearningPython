velo = float(input('Qual a velocidade do veiculo em KM/hora? '))

if velo>80:
    multa = (velo-80)*7
    print('Vc ultrapossou os 80Km/h, sua multa é de R${:.2f}'.format(multa))
else:
    print('Parabéns!, Vc não ultrapassou a velocidade máxima permitida')
print('Dirija com Segurança!')
