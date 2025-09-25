from datetime import datetime
import random

print()
print('-=-' * 20)
nome_usuario = input('Nome de usuario: ').strip()

idade = int(input('Idade: '))

horaAtual = datetime.now()
horaAtualBr = horaAtual.strftime('%d/%m/%Y')

cartoes = ['R$50,00','R$250,00','R$120,00']
sorteio = random.choice(cartoes)

data_de_aniversario = input('Data de nascimento(dd/mm/aaaa): ')
dataAniversario_format = datetime.strptime(data_de_aniversario, '%d/%m/%Y')

print('-=-' * 20)
print()
print()
print('-=-' * 30)
print('Ola {}, seu registro foi cadastrado com sucesso no dia {}!!!'.format(nome_usuario, horaAtualBr))
print('Parabens, houve um sorteio e você ganhou um cartão de compras no valor de {}'.format(sorteio))
print('-=-' * 30)
print()