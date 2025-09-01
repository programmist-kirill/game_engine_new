import subprocess
import platform
import sys
from pathlib import Path


import compilation_asset
import working_with_the_clipboard

# Инициализация глобальных переменных
directory_to_engine = None
importing_asset_for_engine = None

def initialize():
    global directory_to_engine, importing_asset_for_engine
    
    system = platform.system()
    cache_file = "/temp/directory_to_engine" if system == "Linux" else "C:/windows/directory_to_engine"
    
    try:
        with open(cache_file, "r") as file:
            directory_to_engine = Path(file.read().strip())
    except FileNotFoundError:
        print(f"Ошибка: файл {cache_file} не найден!")
        sys.exit(1)

    sys.path.append(str(directory_to_engine / "Manager_assets" / "Importing_asset"))
    
    try:
        import importing_asset_for_engine
    except ImportError as e:
        print(f"Ошибка загрузки модуля: {e}")
        sys.exit(1)

def write():
    name_asset = input("Введите название ассета: ").strip()
    asset = working_with_the_clipboard.paste()
    
    if not isinstance(asset, str):
        asset = str(asset)
    
    asset_dir = directory_to_engine / "Asset"
    asset_dir.mkdir(exist_ok=True)
    
    asset_file = asset_dir / f"{name_asset}.asset"
    
    try:
        asset_file.write_text(asset)
        importing_asset_for_engine.add_asset(name_asset, str(asset_file))
        print(f"Ассет успешно сохранён: {asset_file}")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

def draw_asset(first_value, second_value, index):
    try:
        if index != 0:
            subprocess.run(['wl-copy', '--clear'])
        else:
            print("index == 0")
        # Получаем координаты
        x_old = compilation_asset.obtaining_the_necessary_information.options(first_value)
        y_old = compilation_asset.obtaining_the_necessary_information.determing_y_coordinates(first_value)
        
        # Получаем пробелы и переносы строк
        x = str(compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.space(x_old))
        y = str(compilation_asset.obtaining_the_necessary_information.definition_what_line_breaks.down(y_old))

        # Получаем информацию об ассете
        asset_info = importing_asset_for_engine.getting_asset_by_index(second_value)
        if not asset_info:
            print("Ассет не найден!")
            return

        # Очищаем путь и проверяем файл
        asset_path = Path(asset_info['directory'].strip())
        if not asset_path.exists():
            print(f"Файл ассета не найден: {asset_path}")
            return

        # Читаем содержимое файла
        with open(asset_path, 'r') as f:
            file_asset = f.read().strip()

        print(f"x: '{x}', y: '{y}', file_asset: '{file_asset}'")  # Отладочный вывод

        # Формируем новый ассет
        if index == 0:
            new_asset = f"{y}{x}{file_asset}"
        else:
            clipboard_content = working_with_the_clipboard.paste()
            new_asset = f"{clipboard_content}{y}{x}{file_asset}"

        print(f"Сформированный ассет: '{new_asset}'")  # Отладочный вывод
        
        # Копируем в буфер
        working_with_the_clipboard.copy(new_asset)
        
    except Exception as e:
        print(f"Ошибка в draw_asset: {str(e)}")
# Инициализация при импорте
initialize()