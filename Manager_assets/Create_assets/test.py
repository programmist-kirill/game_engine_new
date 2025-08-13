import sys

import compilation_asset
import working_with_the_clipboard

sys.path.append("/home/kirill/game_engine_new/Manager_assets/Importing_asset/")
import importing_asset_for_engine

def draw_asset(first_value , second_value):
    x_old = compilation_asset.obtaining_the_necessary_information.options(first_value)
    y_old = compilation_asset.obtaining_the_necessary_information.determing_y_coordinates(first_value)
    x = compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.space(x_old)
    y = compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.down(y_old)

    directory_asset = importing_asset_for_engine.getting_asset_by_index(second_value)
    with open(directory_asset , "r") as file:
        file_asset = file.read()
    
    asset = y + x + file_asset

    working_with_the_clipboard.endless_work.copy(asset)