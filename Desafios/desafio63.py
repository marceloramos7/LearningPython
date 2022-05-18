print('--'*13)
print('  Sequência de FIBONACCI')
print('--'*13)
n = int(input("Quantos termos vc quer mostrar: "))
t1=0
t2=1
print('{} -> {}'.format(t1, t2, end=''))
count=3

while count <= n:
    t3 = t2 + t1
    t1 = t2
    t2 = t3
    count += 1
    print('{} -> '.format(t3), end='')

print('FIM')