import os
import platform
import sys
from pathlib import Path

def getting_indexes():
    # Получение пути к движку
    system = platform.system()
    cache_file = "/temp/directory_to_engine" if system == "Linux" else "C:/windows/directory_to_engine"
    
    try:
        with open(cache_file, "r") as file:
            directory_to_engine = Path(file.read().strip())
    except FileNotFoundError:
        print(f"Ошибка: файл {cache_file} не найден!")
        return

    # Настройка путей импорта
    sys.path.append(str(directory_to_engine / "Manager_assets" / "Importing_asset"))
    
    try:
        import importing_asset_for_engine
        from my_module_start import write, draw_asset
    except ImportError as e:
        print(f"Ошибка загрузки модулей: {e}")
        return

    # Инициализация кэша
    cache_dir = directory_to_engine / "Cache"
    cache_dir.mkdir(exist_ok=True)
    cache_index_path = cache_dir / "index_draw_asset"

    index = 0
    while True:
        try:
            # Обработка ввода пользователя
            user_input = input("Введите индекс из таблицы (или exit для сохранения): ").strip()
            
            if user_input.lower() == "exit":
                write()
                break

            index_of_the_element_in_the_table = int(user_input)

            # Выбор ассета
            while True:
                asset_input = input("Введите индекс ассета (L для списка): ").strip().lower()
                
                if asset_input == "l":
                    importing_asset_for_engine.print_full_asset_list()
                    continue
                    
                try:
                    index_of_an_existing_asset = int(asset_input)
                    break
                except ValueError:
                    print("Ошибка: введите число или 'L'")

            # Обработка ассета
            asset_info = importing_asset_for_engine.getting_asset_by_index(index_of_an_existing_asset)
            if not asset_info:
                print(f"Ассет с индексом {index_of_an_existing_asset} не найден")
                continue
                
            # Очистка пути от лишних символов
            asset_path = Path(asset_info['directory'].strip())
            if not asset_path.exists():
                print(f"Файл ассета не найден: {asset_path}")
                continue

            draw_asset(
                first_value=index_of_the_element_in_the_table,
                second_value=index_of_an_existing_asset,
                index=index
            )
            
            index += 1
            cache_index_path.write_text(str(index))
            

        except ValueError:
            print("Ошибка: введите число или 'exit'")
        except Exception as e:
            print(f"Ошибка при обработке: {e}")

if __name__ == "__main__":
    getting_indexes()