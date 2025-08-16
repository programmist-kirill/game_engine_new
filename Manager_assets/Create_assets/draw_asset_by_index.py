import platform
import sys

import my_module_start

system = platform.system()
if system == "Linux":
    with open("/temp/directory_to_engine" , "r") as file:
        directory_to_engine = file.read().replace('\n', '')

elif system == "Windows":
    with open("C:/windows/directory_to_engine" , "r") as file:
        directory_to_engine = file.read().replace('\n', '')
    
sys.path.append(directory_to_engine + "Manager_assets/Importing_asset/")
import importing_asset_for_engine

def getting_indexes():
    index = 0

    work = True
    while work == True:

        index_of_the_element_in_the_table = input("Введите индекс из таблицы , там где нужно использовать ассет . Введите exit чтобы выйти - ")
        if index_of_the_element_in_the_table == "exit" or index_of_the_element_in_the_table == "Exit" or index_of_the_element_in_the_table == "EXIT":
            my_module_start.write()

            work = False
            break

        index_of_an_existing_asset = input("Введите индекс ассета который вы хотите использовать . Введите L чтобы вывести весь список ассетов - ")
        if index_of_an_existing_asset == "L" or index_of_an_existing_asset == "l":
            importing_asset_for_engine.print_full_asset_list()

            index_of_an_existing_asset = input("\n\n\nВведите индекс ассета который вы хотите использовать - ")

        index += 1
        #!start_compilation_asset_module.draw_asset(first_value=index_of_the_element_in_the_table , second_value=index_of_an_existing_asset)
getting_indexes()