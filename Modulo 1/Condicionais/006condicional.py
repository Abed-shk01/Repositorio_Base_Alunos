# Crie um codigo de python que peça o valor da conta, se for maior que 100,00
#adcione uma gorjeta de 10% e exiba o total a pagar
# Caso contrario, adicione uma gorjeta de 5%

#Etapas para resolução
# 1) soliciar o valor  da conta para o usuario
# 2) se a conta for maior que 100 adicionar 10% de gorjeta e apresentar o total a pagar
# 3) se a conta for menor que 100 adicionar 5% de gorjeta e apresentar o total a pagar.
valor_conta = float(input("Digite o valor da conta: R$"))
if valor_conta > 100:
    gorjeta = valor_conta * 0.10
else:
    gorjeta = valor_conta * 0.05
