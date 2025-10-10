import pyautogui
import webbrowser
import time

# agora abrir o Youtube com um video especifico

url = 'https://www.youtube.com/watch?v=TrdHeYhD-qI'
webbrowser.open(url)
time.sleep(5)
pyautogui.press('space')