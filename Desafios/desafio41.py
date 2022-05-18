nome = input('Bom dia, qual seu nome? ')
nasc = int(input('{} qual o ano do seu nascimento? '.format(nome)))
idade = 2022-nasc

if idade<=9:
    print('{} vc será da categoria MIRIM'.format(nome))
elif idade>9 and idade<=14:
    print('{} vc será da categoria INFANTIL'.format(nome))
elif idade>14 and idade<=19:
    print('{} vc será da categoria JUNIOR'.format(nome))
elif idade>19 and idade<=20:
    print('{} vc será da categoria SÊNIOR'.format(nome))
elif idade>20:
    print('{} vc é da categoria MASTER'.format(nome))
print('Boa prova!')
