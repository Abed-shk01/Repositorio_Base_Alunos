# Criar arquivo, recebend informação do usuário
nome = input('Digite seu nome completo: ')
email = input('Digite seu email: ')

# criar arquivo

arquivo = open('pessoa.txt', 'a', encoding='utf-8') # aqui estamos criando o arquivo e armazenando na variavel arquivo. o modo ' escreve sempre no final.
# encoding utf-8 é para utilizar o conjunto de carcateres que engloba a língua portuguesa. e o '\n'

arquivo.write(nome + '|' + email + '\n')# é para pular linha
arquivo.close() # .close() é para fechar o arquivo.

