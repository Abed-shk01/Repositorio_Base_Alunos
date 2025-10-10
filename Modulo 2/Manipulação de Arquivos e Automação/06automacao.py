import pyautogui
import time

print('Você tem 5 segundos para posicionar o mouse no botão escrever...')
time.sleep(5)
print('Posição do mouse', pyautogui.position()) # Comando para encontrar a posição x e y do mouse para automação