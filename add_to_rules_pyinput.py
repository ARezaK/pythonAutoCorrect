from pynput import keyboard
import time
from globals_ import *

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='4')}
]

# The currently active modifiers
current = set()





def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        print(current)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()
        current.clear()


def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print('here')
