import sys
import platform

import compilation_asset
import working_with_the_clipboard
import draw_asset_by_index


def write():
    name_asset = input("Введите название ассета - ")
    asset = working_with_the_clipboard.paste()

    directory_for_write = directory_to_engine + "Asset/" + name_asset + ".asset"
    with open(directory_for_write , "w") as fp:
        fp.write(asset)
    

    importing_asset_for_engine.add_asset(name_asset , directory_asset=directory_for_write)


system = platform.system()

if system == "Linux":
    with open("/temp/directory_to_engine" , "r") as file:
        directory_to_engine = file.read()
    
    sys.path.append(directory_to_engine + "Manager_assets/Importing_asset/")
    import importing_asset_for_engine

elif system == "Windows":
    with open("C:/windows/directory_to_engine" , "r") as file:
        directory_to_engine = file.read()
    
    sys.path.append(directory_to_engine + "Manager_assets/Importing_asset/")
    import importing_asset_for_engine

def draw_asset(first_value , second_value , index):
    if index == 0:
        # index - это сколько раз запускалась связка для создания ассета
        x_old = compilation_asset.obtaining_the_necessary_information.options(first_value)
        y_old = compilation_asset.obtaining_the_necessary_information.determing_y_coordinates(first_value)
        x = compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.space(x_old)
        y = compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.down(y_old)

        directory_asset_old = importing_asset_for_engine.getting_asset_by_index(second_value)
        directory_asset = directory_asset_old['directory']

        with open(directory_asset , "r") as file:
            file_asset = file.read()
        
        asset = y + x
        asset_new = asset + file_asset

        working_with_the_clipboard.copy(text=asset_new , index=index)
        draw_asset_by_index.getting_indexes()
    
    else:
        asset_clipboard = working_with_the_clipboard.paste()
        x_old = compilation_asset.obtaining_the_necessary_information.options(first_value)
        y_old = compilation_asset.obtaining_the_necessary_information.determing_y_coordinates(first_value)
        x = compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.space(x_old)
        y - compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.down(y_old)

        directory_asset_old = importing_asset_for_engine.getting_asset_by_index(second_value)
        directory_asset = directory_asset_old['directory']

        with open(directory_asset , "r") as file:
            file_asset = file.read()

        asset = asset_clipboard + y + x + file_asset

        working_with_the_clipboard.copy(asset)
