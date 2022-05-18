from datetime import date
ano = int(input('Qual o ano quer analisar? \n Coloque "0" para analisar o ano atual. '))
if ano==0:
    ano = date.today().year
if ano % 100 != 0 and ano %4 == 0:
    print('o ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))