import keyboard
import time

flag = False


def execute():
    global flag
    flag = not flag


keyboard.add_hotkey('shift+1', execute)

while 1:
    if flag is True:
        print('true')
        keyboard.press('ctrl')
        time.sleep(0.40)
        keyboard.release('ctrl')
        time.sleep(0.25)
