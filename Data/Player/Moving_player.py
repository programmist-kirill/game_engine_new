import sys

sys.path.append("/home/kirill/game_engine_new/Game_world_editor/Core/")
import Render_core

def right():
    with open("/home/kirill/game_engine_new/Data/Player.asset" , "r") as file:
        player_asset = file.read().strip()
    
    moving = " "

    asset_for_write = moving + player_asset
    
    Render_core.Create_world.Change_scene(asset=asset_for_write)
right()