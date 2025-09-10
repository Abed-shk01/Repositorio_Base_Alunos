# Peça ao usuário para digitiar uma letra 
# se for vogal informe qual vogal
# se for consoante, verifique se é maiúscula ou minuscula
# Solicitação de entrada de dados
letra = input("Digite uma letra")

if letra.lower() in "aeiou" #Lower transforma todas as letras maiusculas em minusculas


    print(f"Vogal: {letra}")
else:
    if letra.isupper(): # isupper identifica se  letra está em maiúscula.
        print(f' Consoante maiúscula {letra}')
    else:
        print(f"Consoante maiúscula {letra}")
    
