n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi a sua segunda nota? '))
media = (n1+n2)/2

if media < 5:
    print('Sua média foi {}, vc foi reprovado!'.format(media))
elif media>7:
    print('Sua média foi de {}, parabéns vc foi aprovado.'.format(media))
elif media > 5 and media < 6.9:
    print('Sua média foi de {}, vc está em recuperação'.format(media))
print('--FIM--')
