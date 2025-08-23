import subprocess
import markup_table

directory_to_open_draw_asset = "/home/kirill/game_engine_new/Game_world_editor/Create_world/index_for_draw_game_world.py"

subprocess.run(["gnome-terminal", "--", "python3", directory_to_open_draw_asset])
markup_table.print_hundred_table()