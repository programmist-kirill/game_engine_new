import os

import math_draw_world
import work_to_clipboard

def processing_end(argument_parameter):
    text = work_to_clipboard.paste()
    name_asset = "Введите название ассета: "
    
    if argument_parameter == "yes":
        directory_parameter = input("Введите директорию параметра - ")
        
        STRING_FOR_WRITE = text + "\n\nparameter=" + directory_parameter

        with open("/home/kirill/game_engine_new/Data/Config/Asset/" + name_asset , "w") as fp:
            fp.write(STRING_FOR_WRITE)
    
    else:
        STRING_FOR_WRITE = text

        with open("/home/kirill/game_engine_new/Data/Config/Asset/" + name_asset , "w") as fp:
            fp.write(STRING_FOR_WRITE)
        

def processing(first_value , second_value , index):
    x_old = math_draw_world.obtaining_the_necessary_information.options(first_value)
    y_old = math_draw_world.obtaining_the_necessary_information.determing_y_coordinates(first_value)
    x = math_draw_world.obtaining_the_necessary_information.definition_what_line_breaks.space(x_old)
    y = math_draw_world.obtaining_the_necessary_information.definition_what_line_breaks.down(y_old)

    if index == 0:
        asset = y + x + second_value
        index += 1
        os.system("wl-copy --clear")
        work_to_clipboard.copy(asset)
    else:
        asset_clipboard = work_to_clipboard.paste()
        asset = asset_clipboard + y + x + second_value
        work_to_clipboard.copy(asset)

def getting_indexes():
    index = 0
    while True:
        index_of_the_element_in_the_table = input("Введите индекс из таблицы (или exit для сохранения): ").strip()
        if index_of_the_element_in_the_table.lower() == "exit":
            
            what_parameter = input("хотите ли вы использовать для этого ассета параметр (Y или N) - ")
            if what_parameter.lower() == "y":
                argument_parameter = "yes"
            else:
                argument_parameter = "no"

            index = "exit"
            processing_end(argument_parameter)
            break

        index_of_an_existing_asset = input("Введите индекс ассета (или L чтобы получить список ассетов): ").strip()
        if index_of_an_existing_asset.lower() == "l":
            with open("/home/kirill/game_engine_new/Asset/Asset.list" , "r") as file:
                asset_list = file.read().strip()
            print(asset_list)
        
        processing(
            first_value=index_of_the_element_in_the_table,
            second_value=index_of_an_existing_asset,
            index=index
        )