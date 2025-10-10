# efeito matrix

import pyautogui, time, random

time.sleep(3)
chars = '01'
for i in range(200):
    pyautogui.write(random.choice(chars), interval= 0.03)