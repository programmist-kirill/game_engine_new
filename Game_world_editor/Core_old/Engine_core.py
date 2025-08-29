"""
управление всеми параметрами , конфигами
"""

class Create_configurator:
    def json_config_world(directory_parameters , directory_asset):
        print("1 - после отрисовки ассета")
        print("2 - перед отрисовкой ассета")
        event_parameter_user = input("Когда запускать файл параметра: ")
        
        name_config = input("\nВведите название конфига - ")

        nahalo = "{"
        string_0 = "\tparameters=" + directory_parameters + " , event_parameter=" + event_parameter_user
        string_1 = "\tasset=" + directory_asset
        end = "}"

        string_for_write = nahalo + "\n" + string_0 + "\n" + string_1 + "\n" + end

        DIRECTORY_TO_WRITE = "/home/kirill/game_engine_new/Data/Config/World/" + name_config + ".json"
        with open(DIRECTORY_TO_WRITE , "w") as fp:
            fp.write(string_for_write)
    
    def dll_config_asset(directory_asset):
        directory_parameteres = input("Введите где находится файл параметра для ассета: ")
        name_parameters = input("Введите название для параметра: ")

        DIRECTORY_TO_WRITE = "/home/kirill/game_engine_new/Data/Config/Asset/" + name_parameters + ".dll"
        STRING_FOR_WRITE = "{\n\tasset=" + directory_asset + "\n\tparameter=" + directory_parameteres + "\n}"
        
        with open(DIRECTORY_TO_WRITE , "w") as fp:
            fp.write(STRING_FOR_WRITE)

        def write_list_config(name_parameters):
            name_asset = input("Введите название ассета: ")

            DIRECTORY_FILE = "/home/kirill/game_engine_new/Data/Config/list_config.asset"
            with open(DIRECTORY_FILE , "r") as file:
                list_config_asset = file.read()
            
            STRING_FOR_WRITE = name_asset + " = " + name_parameters

            write_list = list_config_asset + STRING_FOR_WRITE + "\n"

            with open(DIRECTORY_FILE , "w") as fp:
                fp.write(write_list)
        
        write_list_config(name_parameters)

class Load_configurator:
    def load_json_config_world(directory_parameter):
        