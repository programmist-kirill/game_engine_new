import sys
import getpass

import compilation_asset
import working_with_the_clipboard

username = getpass.getuser()

sys.path.append("/home/" + username + "/game_engine_new/Manager_assets/Importing_asset/")
import importing_asset_for_engine

def draw_asset(first_value , second_value , index):
    if index == 0:
        print("dasdosp[]adop[]asdoa]p[dopa][sdoa][sdoa][ssdo][od][od]")
        x_old = compilation_asset.obtaining_the_necessary_information.options(first_value)
        y_old = compilation_asset.obtaining_the_necessary_information.determing_y_coordinates(first_value)
        x = compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.space(x_old)
        y = compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.down(y_old)

        directory_asset = importing_asset_for_engine.getting_asset_by_index(second_value)
        directory_asset = directory_asset['directory']

        print(directory_asset)
        with open(directory_asset , "r") as file:
            file_asset = file.read()
        
        asset = y + x
        asset = asset + file_asset


        working_with_the_clipboard.copy(text=asset, index=index)

    else:
        print("sdolpa[dio[pa]so]")
        asset_clipboard = working_with_the_clipboard.paste()
        x_old = compilation_asset.obtaining_the_necessary_information.options(first_value)
        y_old = compilation_asset.obtaining_the_necessary_information.determing_y_coordinates(first_value)
        x = compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.space(x_old)
        y = compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.down(y_old)

        directory_asset = importing_asset_for_engine.getting_asset_by_index(second_value)
        with open(directory_asset , "r") as file:
            file_asset = file.read()

        asset = asset_clipboard + y + x + file_asset

        working_with_the_clipboard.copy(asset)

def write_asset():
    name_asset = input("Введите название ассета - ")
    asset = working_with_the_clipboard.endless_work.copy("exit")
    username = getpass.getuser()

    with open("/home/" + username + "/game_engine_new/Asset/" + name_asset + ".asset" , "w") as fp:
        fp.write(asset)

    importing_asset_for_engine.add_asset(name_asset , directory_asset="/home/" + username + "/game_engine_new/Asset/" + name_asset + ".asset")

