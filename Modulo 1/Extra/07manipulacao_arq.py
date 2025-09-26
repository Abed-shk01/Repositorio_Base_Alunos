# criar um arquivo que vai chamar nomes.txt
nomes = ['João\n', 'Maria\n','Ana\n'] # criamos uma lista com os nomes que queremos no nosso arquivo
with open('nomes.txt', 'w', encoding='utf-8') as arquivo: # aqui estamo criando  o arquivo 
    arquivo.writelines(nomes) # estamos pedindo para ele escrever
