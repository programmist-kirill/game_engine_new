import os
import sys
import time
import subprocess
from termcolor import colored

sys.path.append("/home/kirill/game_engine_new/Game_world_editor/Core/")
import Render_core

def clear_screen():
    os.system('clear')

def main_game_loop():
    # Инициализация игры
    Render_core.Create_world.Assembling_scene()


    # Главный игровой цикл
    while True:
        clear_screen()



        print('sh phonm')
        # Отрисовываем текущую сцену
        Render_core.Create_world.Change_scene()
        
        # Ждем ввод игрока
        print("\nУправление: d - вправо, a - влево, q - выход")
        
        # Небольшая задержка для плавности
        time.sleep(0.1)

if __name__ == "__main__":
    main_game_loop()