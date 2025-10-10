# Crie uma automação que escreva um texto automaticamente 

import pyautogui
import time

# observação: abrir  um bloco de notas vazio 
# aguarde alguns segundos para você abrir o bloco de notas
time.sleep(5)

# escreva o texto
pyautogui.write('Boa tarde Abed Sheikhi', interval=0.1)