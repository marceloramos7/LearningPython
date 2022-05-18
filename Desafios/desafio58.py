import random
sorteio = random.randrange(1,10)
tentativa=0
valor = int(input('Tente acertar o valor sorteado entre 1 e 10: '))
while valor != sorteio:
    if valor==sorteio:
        tentativa+=1
        print('Parabéns voce acertou.')
    else:
        tentativa+=1
        print('Errou!')
        valor = int(input('Tente acertar o valor sorteado entre 1 e 10: '))
print('Foram necessarios {} tentativa(s).'.format(tentativa+1))