import os
import sys
import platform

import editor_options_asset
import math_draw_world

system = platform.system()
if system == "Windows":
    with open("C:/windows/directory_to_engine" , "r") as file:
        directory_to_engine = file.read().strip()

    directory_to_clipboard = directory_to_engine + "Game_world_editor/"
    sys.path.append(directory_to_clipboard)
    import work_to_clipboard

    directory_to_importing_asset = directory_to_engine + "Importing_asset/"
    sys.path.append(directory_to_importing_asset)
    import importing_asset_for_engine

elif system == "Linux":
    with open("/temp/directory_to_engine" , "r") as file:
        directory_to_engine = file.read().strip()
    
    directory_to_module = directory_to_engine + "Importing_asset/"
    print(directory_to_module)
    import importing_asset_for_engine


class processing_game_world:
    def convert_numbers_to_assets(first_value , second_value , index):
        x_old = math_draw_world.obtaining_the_necessary_information.options(first_value)
        y_old = math_draw_world.obtaining_the_necessary_information.determing_y_coordinates(first_value)
        x = math_draw_world.obtaining_the_necessary_information.definition_what_line_breaks.space(x_old)
        y = math_draw_world.obtaining_the_necessary_information.definition_what_line_breaks.down(y_old)

        file_asset_for_read = importing_asset_for_engine.getting_asset_by_index(second_value)
        file_asset_for_read = file_asset_for_read['directory']

        with open(file_asset_for_read , "r") as file:
            file_asset = file.read().strip()
            
        asset_for_copy = y + x + file_asset

        if index == 0:
            work_to_clipboard.copy(asset_for_copy)
        else:
            asset_clipboard = work_to_clipboard.paste()
            asset_new = asset_clipboard + asset_for_copy

            work_to_clipboard.copy(asset_new)

    def write_config(action):
        directory_to_cache_lite = directory_to_engine + "Cache/config_world.lite"
        directory_to_cache = directory_to_engine + "Cache/world_config.conf"

        if action == "lite":
            config_world = work_to_clipboard.paste()
            with open(directory_to_cache_lite , "w") as fp:
                fp.write(config_world)
        
        elif action == "not_lite":
            with open(directory_to_cache_lite , "r") as file:
                cache_lite = file.read()
            
            with open(directory_to_cache , "w") as fp:
                fp.write(cache_lite)
        

def getting_indexes():
    index = 0
    while True:
        index_of_the_element_in_the_table = input("Введите индекс из таблицы (или exit для сохранения): ").strip()
        if index_of_the_element_in_the_table.lower() == "exit":
            processing_game_world.write_config(action="not_lite")
            break
        
        try:
            index_of_the_element_in_the_table = int(index_of_the_element_in_the_table)
        except ValueError:
            print("Введите число или exit")
            continue

        while True:
            index_of_an_existing_asset = input("Введите индекс ассета (или L чтобы получить список ассетов): ").strip()
            if index_of_an_existing_asset.lower() == "l":
                importing_asset_for_engine.print_full_asset_list()
                continue
            try:
                index_of_an_existing_asset = int(index_of_an_existing_asset)
                break
            except ValueError:
                print("Ошибка: введите число или L")
                continue
        
        directory_to_cache = directory_to_engine + "Cache/index_draw_game_world"
        if os.path.exists(directory_to_cache):
            index += 1
        else:
            with open(directory_to_cache , "w") as fp:
                fp.write(0)

        processing_game_world.convert_numbers_to_assets(first_value=index_of_the_element_in_the_table , second_value=index_of_an_existing_asset , index=index)


#* def processing_config_game_world():