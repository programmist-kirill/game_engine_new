import os

DIRECTORY_CACHE_WHAT_SCENE_TO_RENDER = "/home/kirill/game_engine_new/Cache/what_scene_to_render"
with open(DIRECTORY_CACHE_WHAT_SCENE_TO_RENDER , "r") as file:
    scene_for_render = file.read().strip()

def init():
    os.system("./Init_render_scene.sh")

def main():
    init()

    if scene_for_render == 2:
        os.system("/home/kirill/game_engine_new/Data/-")