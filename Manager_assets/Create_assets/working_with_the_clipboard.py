import os
import sys


def copy(text):
    try:
        os.system(f"wl-copy {text}")
        print(f"text wl-copy = {text}")
    except Exception as error:
        print(f"Ошибка копирования в буфер: {error}")

def paste():
    try:
        string = os.system("wl-paste")
        return string
    except Exception as error:
        print(f"Ошибка чтения из буфера: {error}")
        input("\n\nДля выхода из программы нажмите Enter")
        sys.exit()

