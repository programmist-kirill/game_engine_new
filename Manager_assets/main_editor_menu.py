import os
import platform

def Determining_what_to_do_with_assets():
    system = platform.system()
    if system == "Linux":
        with open("/temp/directory_to_engine" , "r") as file:
            directory_to_engine = file.read().replace('\n', '')

    elif system == "Windows":
        with open("C:/windows/directory_to_engine" , "r") as file:
            directory_to_engine = file.read().replace('\n', '')


    print("1 - Создание ассета")
    

    action = input("Что вы хотите сделать: ")
    if action == "1":
        directory = directory_to_engine + "Manager_assets/Create_assets/" + "open_draw_asset.py"

        os.system("python " + directory)