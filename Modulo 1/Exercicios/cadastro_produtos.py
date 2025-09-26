# Cadastro de produtos com relatorio
# Crie um programa em python que permita cadastrar prdutos, salvar essas informações em um aruivo chamado 
# produtos.txt. o programa deve permitir:
# Inserir o nome do produto e preço
# gravar os produtos no arquivo (um por linha)
# Ler os dados do arquivo e gerar um relatório com:
# - lista de produtos cadastrador, média dos preços
#- o produto mais caro e o mais barato.

# criar o arquivo produtos.txt

with open('produtos.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('café, 36.00\n')
    arquivo.write('chá, 50.00\n')
    arquivo.write('suco, 18.50\n')
    arquivo.write('refrigerante, 6.90\n')
    arquivo.write('Aguá, 6.90\n')
#ler os produtos do arquivo

produtos = []
with open('produtos.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        nome, preço = linha.strip().split(',')
        produtos.append((nome, float(preço)))

# calcular a média mais caro e o mais barato

total = 0 
mais_caro = produtos[0]
mais_barato = produtos[0]

for nome, preço in produtos:
    total+= preço # percorre a lista produtos e soma o preço encontrado
    if preço > mais_caro[1]:
        mais_caro = (nome, preço)
    if preço < mais_barato[1]:
        mais_barato = (nome, preço)

media= total/len(produtos)

# Criar um relatorio
with open('relatorio_preço.txt', 'w', encoding='utf-8') as relatorio:
    relatorio.write('lista de produtos\n')
    for nome, preço in produtos:
        relatorio.write(f'{nome}: R${preço:.2f}')

        relatorio.write(f'\nPreço Médio: R$ {media:.2f}\n')
        relatorio.write(F'Produto mais caro: R$ {mais_caro[0]} R${mais_caro[1]:.2f}\n')
        relatorio.write(F'Produto mais caro: R$ {mais_barato[0]} R${mais_barato[1]:.2f}\n')