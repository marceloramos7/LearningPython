import random
print('=-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*15)

while True:
    maquina = random.randrange(0, 10)
    n=int(input('Digite um valor: '))
    escolha=input('Par ou Ímpar: ').upper().strip()[0]
    resultado = (n + maquina) % 2

    if escolha == 'P' and resultado==0:
        print('VC VENCEU')
        print(f'A maquina escolheu {maquina} e vc {n} o valor {n+maquina} é PAR')

    if escolha=='P' and resultado==1:
        print('VC PERDEU')
        print(f'A maquina escolheu {maquina} e vc {n} o valor {n+maquina} é ÍMPAR')
        break

    if escolha=='I' and resultado==0:
        print('VC PERDEU')
        print(f'A maquina escolheu {maquina} e vc {n} o valor {n + maquina} é PAR')
        break

    if escolha=='I' and resultado==1:
        print('VC VENCEU')
        print(f'A maquina escolheu {maquina} e vc {n} o valor {n + maquina} é ÍMPAR')

print ('FIM DE JOGO')
