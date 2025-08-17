import platform
import os
import sys
import subprocess
from tkinter import Tk, messagebox

def main():

    root = Tk()
    root.withdraw()

    system = platform.system()
    if system == "Linux":
        with open("/temp/directory_to_engine" , "r") as file:
            directory_to_engine = file.read().replace('\n', '')

    elif system == "Windows":
        with open("C:/windows/directory_to_engine" , "r") as file:
            directory_to_engine = file.read().replace('\n', '')
        
    directory_to_draw_asset = directory_to_engine + "Manager_assets/Create_assets/draw_asset_by_index.py"
    directory_to_open_draw_asset = directory_to_engine + "Manager_assets/Create_assets/open_draw_asset.py"
    directory_to_markup_table = directory_to_engine + "Manager_assets/Create_assets/markup_table.py"

    if os.path.exists(directory_to_draw_asset):
        if os.path.exists(directory_to_open_draw_asset):
            subprocess.run(["gnome-terminal", "--", "python3", directory_to_open_draw_asset])
            print("Команда выполнена, код возврата: 0")
        else:
            messagebox.showerror("Ошибка", "Не удаётся найти файл open_draw_asset.py")
    else:
        messagebox.showerror("Ошибка", "Не удаётся найти файл draw_asset_by_index.py")

    if os.path.exists(directory_to_markup_table):
        os.system("/home/kirill/venv/bin/python /home/kirill/game_engine_new/Manager_assets/Create_assets/markup_table.py")
        #subprocess.run(["xdg-open", directory_to_markup_table])
        print("Команда выполнена, код возврата: 0")
    else:
        messagebox.showerror("Ошибка", "Не удаётся найти файл markup_table.py")

    root.destroy()

main()