import init

import os
import sys
import platform


class Init:
    
    def check_StartLog_in_linux():
        if os.path.exists("/temp/start_log"):
            print("Init = True")

        else:
            init.obtaining_the_necessary_information.linux()
            
            with open("/temp/start_log" , "w") as fp:
                fp.write("")
            
    def check_StartLog_in_windows():
        if os.path.exists("C:/windows/start_log"):
            print("Init = True")
        
        else:
            init.obtaining_the_necessary_information.windows()
            
            with open("C:/windows/start_log" , "w") as fp:
                fp.write("")

    def launch_function_depending_on_the_system():        
        System = platform.system()
        
        if System == "Linux":
            Init.check_StartLog_in_linux()
        
        elif System == "Windows":
            Init.check_StartLog_in_windows()


class Defining_the_module_to_run:
    
    def main():
        print("1 - Запустить менеджер ассетов")
        print("2 - Запустить редактор мира (для создания или модернизации игры)")
        
        action = input("Что вы хотите сделать: ")
        if action == "1":
            sys.path.append("Manager_assets/")
            import main_editor_menu
            main_editor_menu.Determining_what_to_do_with_assets()
        
        elif action == "2":
            sys.path.append("Game_world_editor/")
            import main
            #! запуск модуля

Init.launch_function_depending_on_the_system()
Defining_the_module_to_run.main()