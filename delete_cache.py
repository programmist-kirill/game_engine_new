import os
from termcolor import colored

directory_count_word_cache = "/home/kirill/game_engine_new/Cache/count_word.cache"
directory_index_work = "/home/kirill/game_engine_new/Cache/index_work.cache"
directory_space = "/home/kirill/game_engine_new/Cache/space.cache"
directory_player = "/home/kirill/game_engine_new/Cache/Player.asset"
directory_clipboard = "/home/kirill/game_engine_new/Cache/clipboard.tmp"
directory_keyboard = "/home/kirill/game_engine_new/Cache/keyboard.tmp"
directory_index_list = "/home/kirill/game_engine_new/Cache/index_list.render"
directory_index_work_render = "/home/kirill/game_engine_new/Cache/index_work.render"
directory_work = "/home/kirill/game_engine_new/Cache/work.render"
directory_keyboard_work = "/home/kirill/game_engine_new/Cache/keyboard.word"
directory_index_work_render_output = "/home/kirill/game_engine_new/Cache/index_work_render_output"
directory_scene = "/home/kirill/game_engine_new/Cache/scene"
directory_index_work_cache_scene2 = "/home/kirill/game_engine_new/Cache/index_work_cache_scene2"
directory_work_scene2 = "/home/kirill/game_engine_new/Cache/work_scene2"
directory_cache_space_scene2 = "/home/kirill/game_engine_new/Cache/space_scene2"
directory_cache_minus_space_scene2 = "/home/kirill/game_engine_new/Cache/minus_space_scene2"
directory_cache_what_scene_to_render = "/home/kirill/game_engine_new/Cache/what_scene_to_render"
directory_cache_should_the_obstacle_be_rendered = "/home/kirill/game_engine_new/Cache/should_the_obstacle_be_rendered"
directory_cache_action = "/home/kirill/game_engine_new/Cache/action"


if os.path.exists(directory_count_word_cache):
    print(colored(f"    => Delete file {directory_count_word_cache}","yellow"))
    os.remove(directory_count_word_cache)

if os.path.exists(directory_index_work):
    print(colored(f"    => Delete file {directory_index_work}","yellow"))
    os.remove(directory_index_work)

if os.path.exists(directory_space):
    print(colored(f"    => Delete file {directory_space}" , "yellow"))
    os.remove(directory_space)

if os.path.exists(directory_player):
    print(colored(f"    => Delete file {directory_player}" , "yellow"))
    os.remove(directory_player)

if os.path.exists(directory_clipboard):
    print(colored(f"    => Delete file {directory_clipboard}" , "yellow"))
    os.remove(directory_clipboard)

if os.path.exists(directory_keyboard):
    print(colored(f"    => Delete file {directory_keyboard}" , "yellow"))
    os.remove(directory_keyboard)

if os.path.exists(directory_index_list):
    print(colored(f"    => Delete file {directory_index_list}" , "yellow"))
    os.remove(directory_index_list)

if os.path.exists(directory_index_work_render):
    print(colored(f"    => Delete file {directory_index_work_render}" , "yellow"))
    os.remove(directory_index_work_render)

if os.path.exists(directory_work):
    print(colored(f"    => Delete file {directory_work}" , "yellow"))
    os.remove(directory_work)

if os.path.exists(directory_keyboard_work):
    print(colored(f"    => Delete file {directory_keyboard_work}", "yellow"))
    os.remove(directory_keyboard_work)

if os.path.exists(directory_index_work_render_output):
    print(colored(f"    => Delete file {directory_index_work_render_output}", "yellow"))
    os.remove(directory_index_work_render_output)

if os.path.exists(directory_scene):
    print(colored(f"    => Delete file {directory_scene}" , "yellow"))
    os.remove(directory_scene)

if os.path.exists(directory_index_work_cache_scene2):
    print(colored(f"    => Delete file {directory_index_work_cache_scene2}" , "yellow"))
    os.remove(directory_index_work_cache_scene2)

if os.path.exists(directory_work_scene2):
    print(colored(f"    => Delete file {directory_work_scene2}" , "yellow"))
    os.remove(directory_work_scene2)\
    
if os.path.exists(directory_index_work_cache_scene2):
    print(colored(f"    => Delete file {directory_index_work_cache_scene2}" , "yellow"))
    os.removef(directory_index_work_cache_scene2)

if os.path.exists(directory_cache_minus_space_scene2):
    print(colored(f"    => Delete file {directory_cache_minus_space_scene2}" , "yellow"))
    os.remove(directory_cache_minus_space_scene2)

if os.path.exists(directory_cache_what_scene_to_render):
    print(colored(f"    => Delete file {directory_cache_what_scene_to_render}" , "yellow"))
    os.remove(directory_cache_what_scene_to_render)

if os.path.exists(directory_cache_should_the_obstacle_be_rendered):
    print(colored(f"    => Delete file {directory_cache_should_the_obstacle_be_rendered}" , "yellow"))
    os.remove(directory_cache_should_the_obstacle_be_rendered)

if os.path.exists(directory_cache_action):
    print(colored(f"    => Delete file {directory_cache_action}" , "yellow"))
    os.remove(directory_cache_action)