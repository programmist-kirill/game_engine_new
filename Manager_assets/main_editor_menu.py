import os
import sys

def Determining_what_to_do_with_assets():
    print("1 - Создание ассета")
    
    action = input("Что вы хотите сделать: ")
    if action == "1":
        os.system("/home/kirill/game_engine/Manager_assets/Create_assets/dual_file_open")
