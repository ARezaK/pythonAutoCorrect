from pynput.keyboard import KeyCode, Key, Listener, Controller
import time
from globals_ import *
import os


# The key combination to check
COMBINATIONS = [
    ['testing', 'testworkssortanotreally']
]

# The currently active modifiers
current = ''

# Controller
keyboard = Controller()

# load up rules
for f_ in os.listdir(os.path.join(dir_path, rules_folder_name)):
    with open(os.path.join(dir_path, rules_folder_name, f_)) as rules:
        for rule in rules.readlines():
            if rule[0] != ';' and rule[0] != '' and rule[0] != '\n':
                COMBINATIONS.append([rule.split(';')[0], rule.split(';')[1].strip()])



def clear_word(word):
    # backspaces until word is clear
    for i in word:
        print("i: ", i)
        keyboard.press(Key.backspace)
        time.sleep(0.01)


def on_press(key):
    global current

    if key == Key.space:
        print("clear current on space")
        current = ''
        return

    if hasattr(key, 'char'): current += key.char

    print("current", current)

    for COMBO in COMBINATIONS:
        if current.endswith(COMBO[0]):
            print("got match: ", COMBO)
            clear_word(COMBO[0])
            keyboard.type(COMBO[1])
            current = ''


def on_release(key):
    pass


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
