import subprocess

def copy(text):
    try:
        # Убедимся, что text является строкой и обрежем лишнее
        text = str(text).strip()
        # Ограничим длину текста для отладки
        debug_text = text[:50] + "..." if len(text) > 50 else text
        print(f"Пытаемся скопировать: {debug_text}")
        
        # Используем subprocess вместо os.system
        process = subprocess.Popen(['wl-copy'], stdin=subprocess.PIPE)
        process.communicate(input=text.encode('utf-8'))
        
    except Exception as error:
        print(f"Ошибка копирования в буфер: {error}")

def paste():
    try:
        result = subprocess.run(['wl-paste'], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as error:
        print(f"Ошибка чтения из буфера: {error}")
        return ""