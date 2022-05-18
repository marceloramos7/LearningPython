frase = input('Digite uma frase: ').strip() .lower()

print('A letra "a" aparece {} vezes '.format(frase.count('a')))
print('O primeira posicao de "a" é: {}'.format(frase.find('a')+1))
print('A ultmia letra "a" está na posicao: {}'.format(frase.rfind('a')+1))
