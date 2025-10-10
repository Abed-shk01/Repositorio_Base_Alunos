# 1. Crie um programa que use um comando com o Pyautogui para abrir a calculadora do Windows e faça um calculo de 8 + 2 e apresente o resultado.

import pyautogui
pyautogui.press('Win')
pyautogui.sleep(1)
pyautogui.write('Calculadora')
pyautogui.press('Enter')
pyautogui.sleep(1)
pyautogui.write('8 + 2')
pyautogui.sleep(1)
pyautogui.press('Enter') 



