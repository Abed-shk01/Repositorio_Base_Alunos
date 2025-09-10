# Crie um codigo em python que peça um número ao usuario
# E exiba "número par" se ele for divisivel por 2.

#Etapas
# 1) solicitar o numero ao ususario
# 2) verificar se o numero e par ou impar
# 3) informar se o número é par ou ímpar
numero = float(input("Digite um número: "))

if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f"O numero {numero} e impar")