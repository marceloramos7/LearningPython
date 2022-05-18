#Exercício Python #053 - Detector de Palíndromo
frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
if inverso==junto:
    print('Temos um palidromo')
else:
    print('NAO é palidromo')