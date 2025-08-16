import os

def copy(text):
    os.system("wl-copy " + text)

def paste():
    text = os.system("wl-paste")
    return text