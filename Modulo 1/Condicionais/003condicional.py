# Criar condicional um código python se a temperatura está agradavel ou não
#condições
# temperatura >= 30° informar que esta muito quente
# temperatura >= 20° informar que está agradavel
#temperatura >= 10° informar que está muito frio
#etapas de resolução
# 1) solicitar a temperatra para o usuário
# 2) verificar condicional
# 3)imprimir a resposta segundo a temperatura
temperatura = float(input('Digite a temperatura: '))
if temperatura >= 30:
    print(f"A temperatura do dia é {temperatura}°C e o dia está muito quente.")
elif temperatura >= 20:
    print(f"A temperatura do dia é {temperatura} e esta agradável.")
elif temperatura >= 10:
    print(f"A temperatura do dia é {temperatura} e está muito frio")
else:
    print(f"A temperatura do dia é {temperatura} e está muito frio")