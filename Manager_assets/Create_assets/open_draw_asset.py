import subprocess
import platform
from tkinter import Tk , messagebox
import os

root = Tk()
root.withdraw()

system = platform.system()
if system == "Windows":
    with open("C:/windows/directory_to_engine" , "r") as file:
        directory_to_engine = file.read().strip()
elif system == "Linux":
    with open("/temp/directory_to_engine" , "r") as file:
        directory_to_engine = file.read().strip()

if __name__ == "__main__":
    directory_to_start_markup_table = directory_to_engine + "Manager_assets/Create_assets/markup_table.py"
    directory_to_start_draw_asset_by_index_new = directory_to_engine + "Manager_assets/Create_assets/draw_asset_by_index_new.py"

    print(f"directory_0 = {directory_to_start_markup_table}")
    print(f"directory_1 = {directory_to_start_draw_asset_by_index_new}")
    
    if os.path.exists(directory_to_start_markup_table):
        subprocess.run(["gnome-terminal", "--", "python3", directory_to_start_markup_table])
    else:
        messagebox.showerror("Ошибка" , "Не удается найти файл markup_table.py")
    
    if os.path.exists(directory_to_start_draw_asset_by_index_new):
        subprocess.run(["gnome-terminal", "--", "python3", directory_to_start_draw_asset_by_index_new])
    else:
        messagebox.showerror("Ошибка" , "Не удается найти файл draw_asset_by_index_new.py")
    
    root.destroy()