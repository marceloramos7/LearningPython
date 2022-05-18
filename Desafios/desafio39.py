nome = input('Qual seu nome? ')
nascimento = int(input('Qual o ano do seu nascimento? '))

idade = 2022-nascimento

if idade < 18:
    print('{} ainda nao tem idade para se alistar.'.format(nome))
    print('Falta {} anos para vc se alistar.'.format(18-idade))
elif idade>18:
    print('ATENCAO {} voce ja deveria estar alistado!!!'.format(nome))
    print('Vc esta atrasado {} anos.'.format(idade-18))
elif idade == 18:
    print('PARABENS {} vc deve ser alistar este ano.'.format(nome))
print('--FIM--')