import platform
import sys

import start_compilation

# Получаем все атрибуты модуля
all_attributes = dir(start_compilation)

# Фильтруем только функции
functions = [name for name in all_attributes 
    if callable(getattr(start_compilation, name))]

print("Функции в модуле:", functions)


system = platform.system()
if system == "Linux":
    with open("/temp/directory_to_engine" , "r") as file:
        directory_to_engine = file.read()
elif system == "Windows":
    with open("C:/windows/directory_to_engine" , "r") as file:
        directory_to_engine = file.read()

sys.path.append("/home/kirill/game_engine_new/Manager_assets/Importing_asset")
import importing_asset_for_engine

index = 0

def getting_indexes(index):

    work = True
    while work == True:
        index_of_the_element_in_the_table = input("Введите индекс из таблицы , там где нужно использовать ассет . Введите exit чтобы выйти - ")
        if index_of_the_element_in_the_table == "exit" or index_of_the_element_in_the_table == "Exit" or index_of_the_element_in_the_table == "EXIT":
            start_compilation.write_asset()

            work = False
            break

        index_of_an_existing_asset = input("Введите индекс ассета который вы хотите использовать . Введите L чтобы вывести весь список ассетов - ")
        if index_of_an_existing_asset == "L" or index_of_an_existing_asset == "l":
            importing_asset_for_engine.print_full_asset_list()

            index_of_an_existing_asset = input("\n\n\nВведите индекс ассета который вы хотите использовать - ")

        start_compilation.draw_asset(index , first_value=index_of_the_element_in_the_table , second_value=index_of_an_existing_asset)
        index += 1
        continue

getting_indexes(index)