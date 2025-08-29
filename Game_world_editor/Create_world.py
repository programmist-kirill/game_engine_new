import sys
import os

sys.path.append("/home/kirill/game_engine_new/Game_world_editor/Create_world/")
import math_draw_world

sys.path.append("/home/kirill/gen/Importing_asset/")
import importing_asset_for_engine


def math_function(first_value):
    x_old = math_draw_world.obtaining_the_necessary_information.options(first_value)
    y_old = math_draw_world.obtaining_the_necessary_information.determing_y_coordinates(first_value)
    x = math_draw_world.obtaining_the_necessary_information.definition_what_line_breaks.space(count_x=x_old)
    y = math_draw_world.obtaining_the_necessary_information.definition_what_line_breaks.down(count_y=y_old)

    return x , y

def save_lite(index_table , index_asset):
    x , y = math_function(first_value=index_table)

    directory_asset_old = importing_asset_for_engine.getting_asset_by_index(index_asset)
    directory_asset = directory_asset_old['directory']
    with open(directory_asset , "r") as file:
        asset = file.read().strip()

    info_for_write = y + x + asset

    with open("/temp/file_level.lite" , "w") as fp:
        fp.write(info_for_write)

def save_file_not_lite(index_table , index_asset):
    with open("/temp/file_level.lite" , "r") as file:
        level_lite = file.read().strip()
    
    directory_asset_old = importing_asset_for_engine.getting_asset_by_index(index_asset)
    directory_asset = directory_asset_old['directory']
    with open(directory_asset , "r") as file:
        asset = file.read().strip()

    x , y = math_function(first_value=index_table)
    level_for_write = level_lite + y + x + asset

    with open("/temp/level_0" , "w") as fp:
        fp.write(level_for_write)
    
    name_level = input("как будет называтся уровень - ")
    os.system("mkdir /home/kirill/game_engine_new/Data/" + name_level)
    os.system("cp /temp/level_0 /home/kirill/game_engine_new/Data/" + name_level + "/")

def Main():
    index = 0
    while True:
        index = input("Введите индекс из таблицы(exit для сохранения) - ")
        if index == "exit":
            save_file_not_lite(index_table=index , index_asset=index_asset)
            break

        index_asset = input("Введите индекс ассета - ")

        save_lite(index_table=index , index_asset=index_asset)
        index += 1
        continue
Main()