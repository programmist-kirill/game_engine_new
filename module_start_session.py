import sys
import os

sys.path.append("/home/kirill/game_engine_new/Game_world_editor/Core/")
import Render_core

Render_core.Master_dll_asset.Init_and_start()
Render_core.Create_world.Assembling_scene()

os.system("sudo /home/kirill/venv/bin/python3.13 /home/kirill/game_engine_new/Data/keyboard.dll")
