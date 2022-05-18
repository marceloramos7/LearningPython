times = ('Corinthians', 'Atlético-MG', 'Bragantino', 'Flamengo', 'Santos', 'Fluminense', 'São Paulo',
         'Coritiba', 'América-MG', 'Botafogo', 'Cuiabá', 'Ceará', 'Internacional', 'Avaí', 'Palmeiras',
         'Juventude', 'Goiás', 'Atlético-GO', 'Fortaleza', 'Athletico-PR')

print(f'Os cincos primeiros são {times[:5]}')
print('=-='*5)
print(f'Os rebaixados são {times[-4:]}')
print('=-='*5)
print(f'Os times em ordem alfabética são {sorted(times)}')
print('=-='*5)
print(f'O time do Santos está na {times.index("Santos")+1} posição')
print('=-='*5)
