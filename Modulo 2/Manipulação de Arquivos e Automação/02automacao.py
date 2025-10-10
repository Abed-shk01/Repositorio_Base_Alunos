# importamos a biblioteca pyautogui Crie uma automação que faça o mouse se mover na dorma de um quadrado
import pyautogui
# Crie uma automação que faça o mouse se mover na dorma de um quadrado

for i in range(10):
    pyautogui.moveTo(100 + 10 * i, 100 + 10 * i, duration = 0.25) # moveTo é um comando de movimento 
    pyautogui.moveTo(200 + 10 * i, 100 + 10 * i, duration = 0.25)
    pyautogui.moveTo(200 + 10 * i, 200 + 10 * i, duration = 0.25)
    # pyautogui.moveTo(x,y,duration = em segundos
    # a função moveTo é para o movimento de mouse 