import os
import platform
import sys

def getting_indexes():
    system = platform.system()
    if system == "Linux":
        with open("/temp/directory_to_engine" , "r") as file:
            directory_to_engine = file.read().strip("\n")
    elif system == "Windows":
        with open("C:/windows/directory_to_engine" , "r") as file:
            directory_to_engine = file.read().strip("\n")

    sys.path.append(directory_to_engine + "Manager_assets/Importing_asset/")
    import importing_asset_for_engine

    index = 0
    work = True

    while work == True:
        if not os.path.exists(directory_to_engine + "Cache/index_draw_asset"):
            if index == 0:
                with open(directory_to_engine + "Cache/index_draw_asset" , "w") as fp:
                    fp.write("0")
                print("index == 0")
            else:
                print("Error draw_asset_by_index_new.py")
        else:
            print("Not saved file")

        index_of_the_element_in_the_table = input("Введите индекс из таблицы , там где нужно использовать ассет . Или введите exit чтобы сохранить ассет - ")
        if index_of_the_element_in_the_table.lower() == "exit":
            from my_module_start import write
            write()

            work = False
            break

        index_of_an_existing_asset = input("Введите индекс ассета который вы хотите использовать. Введите L чтобы вывести весь список ассетов - ")
        if index_of_an_existing_asset.lower() == "l":
            importing_asset_for_engine.print_full_asset_list()
            
            index_of_an_existing_asset = input("\n\n\nВведите индекс ассета который вы хотите использовать. Введите L чтобы вывести весь список ассетов - ")
        
        from my_module_start import draw_asset

        index_of_the_element_in_the_table = int(index_of_the_element_in_the_table)
        index_of_an_existing_asset = int(index_of_an_existing_asset)

        draw_asset(first_value=index_of_the_element_in_the_table,
                   second_value=index_of_an_existing_asset,
                   index=index)
        index += 1
