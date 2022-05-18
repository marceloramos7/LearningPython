import time
n=int(input('Em qts segundos os fogos vao estourar? '))

for c in range(0, n):
    print('Contagem Regressiva: {}'.format(n-c))
    time.sleep(1)
print('Booommmm')
