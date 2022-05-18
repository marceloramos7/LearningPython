print('Bom dia, vamos iniciar o seu emprestimo.')

nome = input('Qual seu primeiro e ultimo nome? ')
salario = float(input('Qual o valor do seu salario? '))
casa = float(input('Qual o valor do seu imovel? '))
anos = float(input('Voce vai pagar o emprestimo em qts anos? '))

parcela = anos*12
mensalidade = casa/parcela

salarioparte = salario * (30/100)

if mensalidade <= salarioparte:
    print('Olá Sr. {}'.format(nome))
    print('O seu emprestimo foi aprovado \no valor da sua parcela é de {} \ne será divido em {} parcelas'.format(mensalidade,parcela))
else:
    print('Sr. {}, seu emprestimo foi negado'.format(nome))