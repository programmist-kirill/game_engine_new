from compilation_asset import obtaining_the_necessary_information
from clipboard_utils import copy_to_clipboard, paste_from_clipboard
import getpass
import os
import sys

sys.path.append("/home/kirill/game_engine_new/Manager_assets/Importing_asset/")
import importing_asset_for_engine

class AssetManager:
    def __init__(self):
        self.username = getpass.getuser()
        self.assets_dir = f"/home/{self.username}/game_engine_new/Asset/"
        
    def draw_asset(self, first_value, second_value, index):
        """Рисует ассет в указанной позиции"""
        x_old = obtaining_the_necessary_information.options(int(first_value))
        y_old = obtaining_the_necessary_information.determing_y_coordinates(int(first_value))
        x = obtaining_the_necessary_information.definition_what_line_breaks.space(x_old)
        y = obtaining_the_necessary_information.definition_what_line_breaks.down(y_old)

        if index == 0:
            asset = y + x + self._read_asset_file(second_value)
            copy_to_clipboard(asset)
        else:
            asset = paste_from_clipboard() + y + x + self._read_asset_file(second_value)
            copy_to_clipboard(asset)

    def write_asset(self, asset_content):
        """Сохраняет ассет в файл"""
        name = input("Введите название ассета: ")
        filename = os.path.join(self.assets_dir, f"{name}.asset")
        
        with open(filename, "w") as f:
            f.write(asset_content)
        
        return filename

    def _read_asset_file(self, asset_index):
        """Читает файл ассета по индексу"""
        # Здесь должна быть реализация получения пути к файлу ассета
        # Например, из importing_asset_for_engine
        no_directory_asset = 
        with open(asset_path, "r") as f:
            return f.read()