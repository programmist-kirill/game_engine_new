import working_with_the_clipboard

def Change_scene(asset):
    index_work = 0
    index_list = 0
    work = True
    
    while work == True:
        with open("/home/kirill/game_engine_new/Data/Render.conf" , "r") as file:
            file_render_config = file.readlines()
        
        if index_list >= len(file_render_config):
            break

        string = file_render_config[index_list].strip()

        if string == "Player.asset":
            string = asset
        
        else:
            directory_to_asset = "/home/kirill/game_engine_new/Data/" + string
            with open(directory_to_asset , "r") as file:
                string = file.read().strip()
                
        if index_work == 0:
            working_with_the_clipboard.copy(string)
        else:
            string_clipboard = working_with_the_clipboard.paste()
            new_string = string_clipboard + "\n" + string
            working_with_the_clipboard.copy(new_string)
        
        index_list += 1
        index_work += 1
        continue

    print("\n\n\n\n" + new_string)
        

Change_scene(asset="d")