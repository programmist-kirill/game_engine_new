import sys
import platform
import os

import compilation_asset
import working_with_the_clipboard

# Перенесём импорт draw_asset_by_index в конец файла
# чтобы избежать циклического импорта

def write():
    name_asset = input("Введите название ассета - ")
    asset = working_with_the_clipboard.paste()
    
    # Преобразуем asset в строку, если это не строка
    if not isinstance(asset, str):
        asset = str(asset)
    
    clean_directory = directory_to_engine.strip()
    asset_dir = os.path.join(clean_directory, "Asset")
    os.makedirs(asset_dir, exist_ok=True)
    
    directory_for_write = os.path.join(asset_dir, f"{name_asset}.asset")
    
    try:
        with open(directory_for_write, "w") as fp:
            fp.write(asset)  # Теперь asset точно строка
        
        importing_asset_for_engine.add_asset(name_asset, directory_asset=directory_for_write)
        print(f"Ассет успешно сохранён: {directory_for_write}")
    except Exception as e:
        print(f"Ошибка при сохранении ассета: {e}")

def draw_asset(first_value, second_value, index):
    try:
        if index == 0:
            x_old = compilation_asset.obtaining_the_necessary_information.options(first_value)
            y_old = compilation_asset.obtaining_the_necessary_information.determing_y_coordinates(first_value)
            x = compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.space(x_old)
            y = compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.down(y_old)

            directory_asset_old = importing_asset_for_engine.getting_asset_by_index(second_value)
            directory_asset = directory_asset_old['directory'].strip('\n')
            print(directory_asset)

            with open(directory_asset , "r") as file:
                file_asset = file.read().strip('\n')

            asset = y + x
            asset_new = asset + file_asset

            working_with_the_clipboard.copy(text=asset_new)
            draw_asset_by_index_new.getting_indexes()
        
        else:
            asset_clipboard = working_with_the_clipboard.paste()

            x_old = compilation_asset.obtaining_the_necessary_information.options(first_value)
            y_old = compilation_asset.obtaining_the_necessary_information.determing_y_coordinates(first_value)
            x = compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.space(x_old)
            y = compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.down(y_old)

            directory_asset_old = importing_asset_for_engine.getting_asset_by_index(second_value)
            directory_asset = directory_asset_old['directory']

            with open(directory_asset , "r") as file:
                file_asset = file.read().strip("\n")

            asset = asset_clipboard + y + x + file_asset

            working_with_the_clipboard.copy(asset)
            

    except AttributeError as e:
        print(f"Ошибка доступа к атрибуту: {e}")
    except Exception as e:
        print(f"Другая ошибка: {e}")

# Инициализация системы
system = platform.system()

if system == "Linux":
    with open("/temp/directory_to_engine", "r") as file:
        directory_to_engine = file.read()
    
    sys.path.append(directory_to_engine + "Manager_assets/Importing_asset/")
    import importing_asset_for_engine

elif system == "Windows":
    with open("C:/windows/directory_to_engine", "r") as file:
        directory_to_engine = file.read()
    
    import draw_asset_by_index_new
    draw_asset_by_index_new.getting_indexes()

    sys.path.append(directory_to_engine + "Manager_assets/Importing_asset/")
    import importing_asset_for_engine

