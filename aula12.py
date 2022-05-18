nome = input('Qual seu nome? ')
if nome == 'Marcelo':
    print('Fala MR7')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é muito popular')
elif nome in 'Mel Melinda':
    print('Seu nome é especial, vc tudo minha filha.')
else:
    print('Tenha um bom dia! {}'.format(nome))

