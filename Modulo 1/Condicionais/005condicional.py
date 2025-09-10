#Crie um código qe verifique se a senha digitada pelo usuario dor "1234", "Acesso permitido"
#Etapas para resolução
# criar variavel e atribuir uma senha atraves de um input
# Atraves de condicional cear se a senha e igual a senha armazenada
# Liberar acesso ao usuario
senha_usuario = "1234"

senha = input("Digite sua senha: ")
if senha == senha_usuario:
    print("acesso liberado")
else:
    print("Acesso negado. Tente novamente")