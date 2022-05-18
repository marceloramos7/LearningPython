n2 = input('Digite algo: ')

print('{} é somente número? ' .format(n2), n2.isnumeric())
print('{} só tem espaços? ' .format(n2), n2.isspace())
print('{} é alfabético? ' .format(n2), n2.isalpha())
print('{} é alfnúmerico? ' .format(n2), n2.isalnum())
print('{} é maiúscula? ' .format(n2), n2.isupper())
print('{} é minúscula? ' .format(n2), n2.islower())
print('{} está capitalizada?  ' .format(n2), n2.istitle())




