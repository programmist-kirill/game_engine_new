import os
import sys

sys.path.append("/home/kirill/gen/Importing_asset/")
import importing_asset_for_engine
from my_module_start import write, draw_asset

def getting_indexes():
    directory_to_engine = "/home/kirill/gen/"
    
    index = 0
    while True:
        user_input = input("Введите индекс из таблицы (или exit для сохранения): ").strip()
        if user_input.lower() == "exit":
            write()
            break

        try:
            index_of_the_element_in_the_table = int(user_input)
        except ValueError:
            print("Ошибка: введите число или 'exit'")
            continue

        while True:
            asset_input = input("Введите индекс ассета (введите L чтобы получить список ассетов): ").strip()
            if asset_input.lower() == "l":
                importing_asset_for_engine.print_full_asset_list()
                continue
            try:
                index_of_an_existing_asset = int(asset_input)
                break
            except ValueError:
                print("Ошибка: введите число или 'L'")

        # Работа с кэшем
        cache_dir = os.path.join(directory_to_engine, "Cache")
        os.makedirs(cache_dir, exist_ok=True)
        cache_file = os.path.join(cache_dir, "index_draw_asset")
        
        if os.path.exists(cache_file):
            index += 1
        else:
            with open(cache_file, "w") as fp:
                fp.write("0")

        draw_asset(
            first_value=index_of_the_element_in_the_table,
            second_value=index_of_an_existing_asset,
            index=index
        )