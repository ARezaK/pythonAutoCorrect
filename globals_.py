from sys import platform as sysplatform
import os
import subprocess
import time

if sysplatform != "darwin":
    import win32clipboard

rules_folder_name = 'rules'

dir_path = os.path.dirname(os.path.abspath(__file__))


def get_clipboard_data():
    if sysplatform == "darwin":  # OSX
        p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
        retcode = p.wait()
        data = p.stdout.read()
    else:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    print("dat: ", data)
    return data


def execute():
    print('executing')
    # grab from clipboard
    data = get_clipboard_data()
    newdata = data

    # wait until clibpard cahnes
    while newdata == data:
        time.sleep(0.5)
        newdata = get_clipboard_data()

    # write it to custom txt
    with open(os.path.join(dir_path, rules_folder_name, 'custom.txt'), 'a') as f:
        f.write(data + ';' + newdata + '\n')
