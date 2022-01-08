import pyautogui as ptg
import time
import pyperclip as pyc

ptg.PAUSE = 1

ptg.press("win")
ptg.write("chrome")
ptg.press("enter")
pyc.copy("https://mail.google.com/mail/u/0/#inbox")
ptg.hotkey("ctrl", "v")
ptg.press("enter")
