import clipboard

def copy(text):
    clipboard.copy(text)

def paste():
    text = clipboard.paste()
    return str(text)  # Преобразуем результат в строку