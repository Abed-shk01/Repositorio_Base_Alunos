# Criar um arquivo chamado mensagem.txt e escrever ua frase

# utilizando a palavra with open() não precisamos usar o close() pois o arquivo sera fechado
# ao final da execução automaticamente por conta do with.

with open('mensagem.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('python facilita a vida')