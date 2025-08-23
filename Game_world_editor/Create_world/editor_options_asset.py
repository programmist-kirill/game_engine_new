import sys
import os
import time

directory_to_engine = "/home/kirill/game_engine_new/"

class init:
    def new_parameter(directory_to_engine):
        name_parametr = input("Введите название параметра для ассета - ")
        directory_user_parametr = input("Введите где находится алгоритм параметра - ")

        if os.path.exists(directory_user_parametr):
            print(f"файл {directory_user_parametr} найден")
        else:
            print(f"файл {directory_user_parametr} не найден")
            directory_user_parametr = input("Введите где находится алгоритм параметра - ")
            
            if os.path.exists(directory_user_parametr):
                print(f"файл {directory_user_parametr} найден")
            else:
                print("-------------------------------\nВыход из программы через 5 секунд\n-------------------------------")
                time.sleep(5)
                sys.exit()
        
        with open(directory_user_parametr , "r") as file:
            parametr_for_write = file.read().strip()
        
        directory_for_write_parametr = directory_to_engine + "set_of_parameters/" + name_parametr + ".dll"
        with open(directory_for_write_parametr , "r") as fp:
            fp.write(parametr_for_write)
        
        return name_parametr

    def add_parameter_to_asset(directory_to_engine):
        name_asset = input("Введите название ассета к которому нужно подцепить параметры - ")
        name_parameter = input("Введите название параметра - ")

        directory_asset = directory_to_engine + "Asset/" + name_asset + ".asset"
        directory_parameter = directory_to_engine + "set_of_parameters/" + name_parameter + ".dll"

        if os.path.exists(directory_asset):
            print(f"файл {directory_asset} бьл найден")
        else:
            name_asset = input("Введите название ассета к которому нужно подцепить параметры - ")
            directory_asset = directory_to_engine + "Asset/" + name_asset + ".asset"
            if os.path.exists(directory_asset):
                print(f"файл {name_asset} был найден")
            else:
                print("-------------------------------\nВыход из программы через 5 секунд\n-------------------------------")
                time.sleep(5)
                sys.exit()
        

        if os.path.exists(directory_parameter):
            print(f"файл {directory_parameter} был найден")
        else:
            name_parameter = input("Введите название параметра - ")
            directory_parameter = directory_to_engine + "set_of_parameters/" + name_parameter + ".dll"
            if os.path.exists(directory_parameter):
                print(f"файл {directory_parameter} был найден")
            else:
                print("-------------------------------\nВыход из программы через 5 секунд\n-------------------------------")
                time.sleep(5)
                sys.exit()
        

        with open(directory_asset , "r") as file:
            asset = file.read().strip()
        
        asset_new = asset + "\n" + directory_parameter

        with open(directory_asset , "r") as fp:
            fp.write(asset_new)

class module:
    def write_parameter_and_asset(directory_asset , directory_parameter):
        directory_to_engine = "/home/kirill/game_engine_new/"
        directory_to_configurator_file = directory_to_engine + "Cache/config_game_world.conf"
        
        with open(directory_asset , "r") as file:
            asset_file = file.read().strip()
        
        with open(directory_parameter , "r") as file:
            parameter_file = file.read().strip()

        if os.path.exists(directory_to_configurator_file):
            with open(directory_to_configurator_file , "r") as file:
                file_configurator = file.read().strip()
            

            #! --\n {asset} (tab) {parameter=directory} \n--

            file_configurator_new = file_configurator + "\n" + "--\n" + asset_file + "\n" + parameter_file
            with open(directory_to_configurator_file , "w") as fp:
                fp.write(file_configurator_new)

    def write_config_lite():
        directory_to_engine = "/home/kirill/game_engine_new/"
        directory_to_configurator_file_lite = directory_to_engine + "Cache/config_game_world.lite"

        