import os
import platform
import sys

system = platform.system()
if system == "Linux":
    with open("/temp/directory_to_engine", "r") as file:
        directory_to_engine = file.read().strip()  # Удаляем символы новой строки
elif system == "Windows":
    with open("C:/windows/directory_to_engine", "r") as file:
        directory_to_engine = file.read().strip()

sys.path.append(os.path.join(directory_to_engine, "Manager_assets/Importing_asset/"))
import importing_asset_for_engine

def getting_indexes():
    index = 0
    work = True
    
    while work:
        index_of_the_element_in_the_table = input("Введите индекс из таблицы, там где нужно использовать ассет. Введите exit чтобы выйти - ")
        if index_of_the_element_in_the_table.lower() == "exit":
            # Импортируем write только когда нужно
            from my_module_start import write
            write()
            work = False
            break

        index_of_an_existing_asset = input("Введите индекс ассета который вы хотите использовать. Введите L чтобы вывести весь список ассетов - ")
        if index_of_an_existing_asset.lower() == "l":
            importing_asset_for_engine.print_full_asset_list()
            index_of_an_existing_asset = input("\n\n\nВведите индекс ассета который вы хотите использовать - ")

        index += 1
        from my_module_start import draw_asset

        index_of_the_element_in_the_table = int(index_of_the_element_in_the_table)
        index_of_an_existing_asset = int(index_of_an_existing_asset)

        draw_asset(first_value=index_of_the_element_in_the_table, 
                  second_value=index_of_an_existing_asset, 
                  index=index)

if __name__ == "__main__":
    getting_indexes()