from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

conf = 0.8

# funcao para clicar no botao
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# laco que mantem o programa rodando ate o usuario apertar 'm'
while keyboard.is_pressed('m') == False:
    if pyautogui.locateOnScreen('aceitar.png', confidence = conf) != None:
        botao = pyautogui.locateOnScreen('aceitar.png', grayscale = True, confidence = conf)
        click(botao.left + int(botao.width/2), botao.top + int(botao.height/2)) #o calculo e so para achar o meio do botao
        time.sleep(1)
