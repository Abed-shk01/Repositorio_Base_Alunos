# ler um arquivo

arquivo = open('pessoa.txt', 'r') # a leitura  está sendo feita na memorioa, como se o robo estivesse lendo só para ele.
conteudo = arquivo.read() # eu armazeno a leitura em uma variavel.
print(conteudo) # sem o print eu não conseguirei ver oque está armazenado
arquivo.close # sempre que usarmos a função open devemos usar a função close tambem