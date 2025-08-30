import os

def determing_index_work():
    if os.path.exists("/home/kirill/game_engine_new/Cache/index_work_render_output"):
        index_work = 1
    else:
        index_work = 0
        with open("/home/kirill/game_engine_new/Cache/index_work_render_output" , "w") as fp:
            fp.write("0")
    return index_work

def main():
    DIRECTORY_TO_SCENE = "/home/kirill/game_engine_new/Cache/scene"

    index_work = determing_index_work()

    while True:
        if os.path.exists(DIRECTORY_TO_SCENE):
            with open("/home/kirill/game_engine_new/Cache/scene" , "r") as file:
                scene = file.read()
            
            os.remove(DIRECTORY_TO_SCENE)

        else:
            continue

        
        if index_work == 1:
            os.system("clear")
            print(scene)
            continue
        else:
            print(scene)
            index_work += 1
            continue

main()