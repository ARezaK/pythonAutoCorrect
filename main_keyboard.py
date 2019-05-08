import keyboard
from globals_ import *

COMBINATIONS = [
    ['testing1234', 'testingworks']
]


for f_ in os.listdir(os.path.join(dir_path, rules_folder_name)):
    with open(os.path.join(dir_path, rules_folder_name, f_)) as rules:
        for rule in rules.readlines():
            if rule[0] != ';' and rule[0] != '' and rule[0] != '\n':
                COMBINATIONS.append([rule.split(';')[0], rule.split(';')[1].strip()])


for COMBO in COMBINATIONS:
    keyboard.add_abbreviation(COMBO[0], COMBO[1] + ' ', True, 3)


keyboard.add_hotkey('shift+4', execute)

print('ready')
while 1:
    pass
