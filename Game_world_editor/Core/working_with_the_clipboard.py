import subprocess

def copy(text):
    try:
        # Убедимся, что text является строкой и обрежем лишнее
        text = str(text).strip()
        # Ограничим длину текста для отладки
        debug_text = text[:50] + "..." if len(text) > 50 else text
        print(f"Пытаемся скопировать: {debug_text}")
        
        # Используем subprocess вместо os.system
        with open("/home/kirill/game_engine_new/Cache/clipboard.tmp" , "w") as fp:
            fp.write(text)
        
    except Exception as error:
        print(f"Ошибка копирования в буфер: {error}")

def paste():
    try:
        with open("/home/kirill/game_engine_new/Cache/clipboard.tmp" , "r") as file:
            clipboard_cache = file.read()
        
        return clipboard_cache
    except Exception as error:
        print(f"Ошибка чтения из буфера: {error}")
        return ""