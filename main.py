print('Olá, bem vindo ao sistema de gerenciamento de clientes!')
nome = input('Seu nome: ')
try: 
    idade = int(input('Sua idade: '))
    n_registro = int(input('Numero de registro: '))
    valor = float(input('Saldo no mês: '))
    print('------------------------')
    print('Dados recebidos: ')
    print('Nome:', nome)
    print('Idade: ', idade)
    print('Numero de registro: ', n_registro)
    print('Saldo: ', valor)
except ValueError:
    print('Valor digitado é inválido!')