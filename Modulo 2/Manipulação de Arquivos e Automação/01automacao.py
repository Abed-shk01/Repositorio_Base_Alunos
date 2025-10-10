# 1ª passo : instalar o pyautogui com o comando pip install pyautogui
# Crie uma automação que abra automaticamente um navegador 
#importamos a biblioteca para o script em uso
import pyautogui

# 'Press' é um comando que utilizamos
# para pressionar a tecla desejada

pyautogui.press('Win') # para pressionar a tecla windows

# 'Sleep' é um comando que utilizamos para deixar o código em espera por alguns segundos 

pyautogui.sleep(1)

# 'Write' é um comando que utilizammos para escrever algo
pyautogui.write('Google Chromw')

pyautogui.press('Enter')