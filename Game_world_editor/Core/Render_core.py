import os
from termcolor import colored

import working_with_the_clipboard

class Manager_temporary_file:
    def Writing_temporary_files(index_work , index_list , work):
        index_work = str(index_work)
        index_list = str(index_list)

        DIRECTORY_INDEX_WORK_CACHE = "/home/kirill/game_engine_new/Cache/index_work.render"
        DIRECTORY_INDEX_LIST_CACHE = "/home/kirill/game_engine_new/Cache/index_list.render"
        DIRECTORY_WORK_CACHE = "/home/kirill/game_engine_new/Cache/work.render"

        with open(DIRECTORY_INDEX_WORK_CACHE , "w") as fp:
            fp.write(index_work)
        with open(DIRECTORY_INDEX_LIST_CACHE , "w") as fp:
            fp.write(index_list)
        with open(DIRECTORY_WORK_CACHE , "w") as fp:
            fp.write(work)

    def Reading_temporary_files():
        DIRECTORY_INDEX_WORK_CACHE = "/home/kirill/game_engine_new/Cache/index_work.render"
        DIRECTORY_INDEX_LIST_CACHE = "/home/kirill/game_engine_new/Cache/index_list.render"
        DIRECTORY_WORK_CACHE = "/home/kirill/game_engine_new/Cache/work.render"

        if os.path.exists(DIRECTORY_INDEX_WORK_CACHE):
            print(f"{DIRECTORY_INDEX_WORK_CACHE} is found")
        else:
            with open(DIRECTORY_INDEX_WORK_CACHE , "w") as fp:
                fp.write("0")
        
        if os.path.exists(DIRECTORY_INDEX_LIST_CACHE):
            print(f"{DIRECTORY_INDEX_LIST_CACHE} is found")
        else:
            with open(DIRECTORY_INDEX_LIST_CACHE , "w") as fp:
                fp.write("0")
        
        if os.path.exists(DIRECTORY_WORK_CACHE):
            print(f"{DIRECTORY_WORK_CACHE} is found")
        else:
            with open(DIRECTORY_WORK_CACHE , "w") as fp:
                fp.write("True")

        with open(DIRECTORY_INDEX_WORK_CACHE , "r") as file:
            index_work = file.read().strip()
        with open(DIRECTORY_INDEX_LIST_CACHE , "r") as file:
            index_list = file.read().strip()
        with open(DIRECTORY_WORK_CACHE , "r") as file:
            work = file.read().strip()
        
        index_work = int(index_work)
        index_list = int(index_list)

        return index_work , index_list , work


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
        
        os.system("wl-copy --clear")

    def Change_scene():
        global new_string

        index_work, index_list, work = Manager_temporary_file.Reading_temporary_files()
        string_new = ""  # Инициализируем переменную заранее
        
        while work == "True":
            if index_work == 0:
                with open("/home/kirill/game_engine_new/Data/Player.asset", "r") as file:
                    asset = file.read().strip()
            elif index_work > 0:
                # ДОБАВЬТЕ ПРОВЕРКУ СУЩЕСТВОВАНИЯ ФАЙЛА
                cache_player_path = "/home/kirill/game_engine_new/Cache/Player.asset"
                if os.path.exists(cache_player_path):
                    with open(cache_player_path, "r") as file:
                        asset = file.read()
                else:
                    # Если файл не существует, используйте оригинальный asset
                    with open("/home/kirill/game_engine_new/Data/Player.asset", "r") as file:
                        asset = file.read().strip()

            with open("/home/kirill/game_engine_new/Data/Render.conf", "r") as file:
                file_render_config = file.readlines()
            
            if index_list >= len(file_render_config):
                print("index_list >= len(file_render_config)")
                break

            string = file_render_config[index_list].strip()
            print(f"string = {string}")

            if string == "Player.asset":
                string = asset
            else:
                directory_to_asset = "/home/kirill/game_engine_new/Data/" + string
                with open(directory_to_asset, "r") as file:
                    string = file.read().strip()

            if index_work == 0:
                working_with_the_clipboard.copy(string)
                string_new = string  # Сохраняем значение
            else:
                cache_clipboard = working_with_the_clipboard.paste()
                string_new = cache_clipboard + "\n" + string
                working_with_the_clipboard.copy(string_new)
            
            index_list += 1
            index_work += 1
            
            Manager_temporary_file.Writing_temporary_files(index_work=index_work, index_list=index_list, work=work)

            #? os.system("python /home/kirill/game_engine_new/delete_cache.py")

            continue

        with open("/home/kirill/game_engine_new/Cache/scene" , "w") as fp:
            fp.write(string_new)

        os.system("sudo /home/kirill/venv/bin/python3.13 /home/kirill/game_engine_new/Data/keyboard.dll")

        
    
    def Update_scene():
        """Обновляет и перерисовывает сцену"""
        global new_string
        
        index_work, index_list, work = Manager_temporary_file.Reading_temporary_files()
        string_new = ""
        
        # Сбрасываем индекс для перерисовки всей сцены
        index_list = 0
        index_work = 0
        work = "True"
        
        Manager_temporary_file.Writing_temporary_files(index_work, index_list, work)
        
        # Перерисовываем сцену
        Create_world.Change_scene()