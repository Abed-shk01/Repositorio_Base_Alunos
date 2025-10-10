# Automatização de login ficticio
# ideia : preencher automaticamente um formulario
#(HTML local ou simulado, via bloco de notos).

import pyautogui, time 
pyautogui.sleep(3)
pyautogui.write('Aluno_python', interval=0.1)
pyautogui.press('tab')
pyautogui.write('Senha123', interval=0.1)
pyautogui.press("enter")
