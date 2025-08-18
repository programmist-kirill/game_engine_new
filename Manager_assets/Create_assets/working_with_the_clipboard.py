import subprocess

def copy(text):
    try:
        # Преобразуем в строку и убираем переносы
        text = str(text).replace('\n', ' ')
        subprocess.run(['wl-copy'], input=text.encode('utf-8'), check=True)
        print(f"Скопировано в буфер: {text}")
    except Exception as error:
        print(f"Ошибка копирования: {error}")

def paste():
    try:
        result = subprocess.run(['wl-paste'], capture_output=True, text=True, check=True)
        return result.stdout.strip()  # Убираем переносы строк
    except Exception as error:
        print(f"Ошибка чтения буфера: {error}")
        return ""