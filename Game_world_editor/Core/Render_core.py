import os
from termcolor import colored
import working_with_the_clipboard

def get_assets_without_extension(filename='/home/kirill/game_engine_new/Data/Render.conf'):
    """
    Читает файл Render.conf и возвращает список имен файлов без расширений.
    
    Args:
        filename (str): Путь к файлу Render.conf
        
    Returns:
        list: Список имен файлов без расширений
    """
    assets = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                # Пропускаем пустые строки и строки без точки (нет расширения)
                if line and '.' in line:
                    # Разделяем по точке и берем первую часть
                    asset_name = line.split('.')[0]
                    assets.append(asset_name)
    
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    
    return assets


class Master_dll_asset:
    def Init_and_start():
        index_list = 0
        work = True

        list_asset = get_assets_without_extension("/home/kirill/game_engine_new/Data/Render.conf")
        
        while work == True:
            try:
                file_for_start_old = list_asset[index_list]
            except Exception as e:
                work = False
                break

            file_for_start = "/home/kirill/game_engine_new/Data/" + file_for_start_old + ".dll"
            if os.path.exists(file_for_start):
                os.system("python " + file_for_start)
            else:
                print(f"{file_for_start} не существует")
            
            index_list += 1
            continue
    
    def Start_dll(name_asset):
        file_for_start = "/home/kirill/game_engine_new/Data/" + name_asset + ".dll"
        if os.path.exists(file_for_start):
            os.system("python " + file_for_start)
        else:
            print(colored(f"{file_for_start} Not found , please create","red"))

class Create_world:
    def Assembling_scene():
        with open("/home/kirill/game_engine_new/Data/Render.conf" , "r") as file:
            file_render_config = file.readlines()
        
        index_work = 0
        index_list = 0
        work = True
        asset_new = ""
        
        while work == True:
            # Проверяем, не вышли ли за пределы списка
            if index_list >= len(file_render_config):
                break
                
            string = file_render_config[index_list].strip()
            
            if string != "":
                directory_asset = "/home/kirill/game_engine_new/Data/" + string
                
                if os.path.exists(directory_asset):
                    with open(directory_asset , "r") as file:
                        asset = file.read().strip()

                    if index_work == 0:
                        working_with_the_clipboard.copy(asset)
                        asset_new = asset
                    else:
                        asset_clipboard = working_with_the_clipboard.paste()
                        asset_new = asset_clipboard + "\n" + asset
                        working_with_the_clipboard.copy(asset_new)
                    
                    index_list += 1
                    index_work += 1
                    continue
                else:
                    index_list += 1
                    continue
            else:
                print("\n\n\n\n\n\n\n\n" + asset_new + "\n\n\n\n\n\n\n\n")
                print(f"index_list = {index_list}")
                print(f"index_work = {index_work}")
                work = False
                break
        
        if work:
            print("\n\n\n\n\n\n\n\n" + asset_new + "\n\n\n\n\n\n\n\n")
            print(f"index_list = {index_list}")
            print(f"index_work = {index_work}")
    
    def Change_scene(asset):


        with open("/home/kirill/game_engine_new/Data/Render.conf" , "r") as file:
            file_render_config = file.readlines()

        index_work = 0
        index_list = 0
        work = True
        asset_new = ""

        while work:
            if index_list >= len(file_render_config):
                break

            string = file_render_config[index_list].strip()

            if string != "":
                # Проверяем, является ли строка "Player.asset"
                if string == "Player.asset":
                    print(colored(f"🎮 Обнаружен Player.asset! Asset: {asset}", "green", attrs=["bold"]))
                
                if string == "Player.asset" or string == "intelection":
                    directory_asset = "/home/kirill/game_engine_new/Cache/" + asset + ".asset"

                    if os.path.exists(directory_asset):
                        with open(directory_asset, "r") as file:
                            asset_content = file.read().strip()
                        
                        if index_work == 0:
                            working_with_the_clipboard.copy(asset_content)
                            asset_new = asset_content
                        else:
                            asset_clipboard = working_with_the_clipboard.paste()
                            asset_new = asset_clipboard + "\n" + asset_content
                            working_with_the_clipboard.copy(asset_new)
                        
                        index_list += 1
                        index_work += 1
                        continue
                    else:
                        index_list += 1
                        continue
                else:
                    # Пропускаем другие asset'ы
                    index_list += 1
                    continue
            else:
                work = False
                break