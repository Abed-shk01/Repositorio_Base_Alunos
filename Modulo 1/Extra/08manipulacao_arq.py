# Contar linhas de um arquivo

with open('pessoa.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()# aqui estamos lendo o arquivo armazenado a leitrua varia
    
    print('total linhas: ', len(linhas)) # função len é uma função que conta ent len(linhas) = 'contar linhas'