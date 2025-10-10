# Desenhar um objeto
# Abrir bloco de notas para executar o desenho

import pyautogui
import time

pyautogui.press('win')
time.sleep(1)

pyautogui.write('Desenhando com pyautogui')
pyautogui.press('enter')
pyautogui.sleep(2)
carinha = []

'        |'                 '|'
'        |  --         --    |'
'        |   °        °      |'
'        |'                 '|'
'        |   \__________/    |'           
'        |'                 '|'
'        |__________________ |'
for linha in carinha:
    pyautogui.write(linha, interval=0.1)
    pyautogui.press('enter')
print(' O desenho da carinha foi concluído!')