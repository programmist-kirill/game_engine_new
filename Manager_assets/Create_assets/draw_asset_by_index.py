import platform
import sys

system = platform.system()
if system == "Linux":
    with open("/temp/directory_to_engine" , "r") as file:
        directory_to_engine = file.read()
elif system == "Windows":
    with open("C:/windows/directory_to_engine" , "r") as file:
        directory_to_engine = file.read()

sys.path.append(directory_to_engine + "Manager_assets/Importing_asset/")
#!import importing_an_asset_for_the_engine_to_work

sys.path.append(directory_to_engine + "Manager_assets/")
import compilation_asset


def getting_indexes():
    work = True
    while work == True:
        index_of_the_element_in_the_table = input("Введите индекс из таблицы , там где нужно использовать ассет . Введите exit чтобы выйти - ")
        if index_of_the_element_in_the_table == "exit" or index_of_the_element_in_the_table == "Exit" or index_of_the_element_in_the_table == "EXIT":

            work = False
            break

        index_of_an_existing_asset = input("Введите индекс ассета который вы хотите использовать . Введите L чтобы вывести весь список ассетов - ")
        if index_of_an_existing_asset == "L" or index_of_an_existing_asset == "l":
            #!importing_an_asset_for_the_engine_to_work.AssetManager.get_all_asset_list()

            index_of_an_existing_asset = input("\n\n\nВведите индекс ассета который вы хотите использовать - ")

        compilation_asset.compilation_asset.launch_the_required_function(first_value=index_of_the_element_in_the_table)
        continue

getting_indexes()