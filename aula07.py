nome = input('Qual seu nome? ')
print('Prazer {:=^10} !'  .format(nome))

n1 = int(input('{} digite um valor: '.format(nome)))
n2 = int(input('{} digite outro valor: '.format(nome)))

s = n1+n2
m = n1*n2
su = n1-n2
d = n1/n2
di = n1//n2
e = n1**n2

print('A soma vale: {}'.format(s))
print('A subtração é: {}'.format(su))
print('O produto é: {}'.format(m))
print('A divisão é: {:2f} e a divisão inteira é {} '.format(d, di))
print('A exponenciação é: {}'.format(e))
