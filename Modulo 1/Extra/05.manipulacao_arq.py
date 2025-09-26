# ler e imprimir o conteúdo do arquivo mensagem.txt

with open('mensagem.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read()) # aqui estamos imprimindo o que o arquivo leu
# e neste caso não estamos armazenandoem nenhuma variavel