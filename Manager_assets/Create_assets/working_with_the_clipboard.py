import pyperclip

def copy_to_clipboard(text):
    """Копирует текст в буфер обмена"""
    pyperclip.copy(text)

def paste_from_clipboard():
    """Вставляет текст из буфера обмена"""
    return pyperclip.paste()