# Adicionar uma nova frase ao meu arquivo
# Caso eu queira adicionar uma nova frase no arquivo já criado 
# utilizamos o modo 'a' para não substituir oque já tem lá

with open('mensagem.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('\naprendendo a manipular arquivos.')

    with open('mensagem.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write('\npython é interessante.')