import getpass

class parse_dict:
    @staticmethod
    def main(input_string):    
        parts = input_string.split(' = ')
        if len(parts) >= 3:  # Проверяем, что строка содержит все необходимые части
            result_dict = {
                'index': parts[0],
                'name': parts[1],
                'directory': parts[2]
            }
            result_dict = result_dict
            print(result_dict)
            return result_dict
        return None

    @staticmethod
    def check(input_string, index_for_search):
        parts = input_string.strip().split(' = ')  # Добавляем strip() здесь
        if parts and parts[0] == str(index_for_search):
            result = parse_dict.main(input_string)
            if result and 'directory' in result:
                result['directory'] = result['directory'].strip('\n')  # Удаляем \n из пути
            return result
        return None

def getting_asset_by_index(index_for_search):
    username = getpass.getuser()
    with open("/home/" + username + "/game_engine_new/Asset/Asset.list", "r") as file:
        asset_list = file.readlines()

    for input_string in asset_list:  # Используем цикл for для безопасного перебора
        result = parse_dict.check(input_string, index_for_search)
        if result is not None:
            return result
    print(f"Asset with index {index_for_search} not found")
    return None

def add_asset(name_asset, directory_asset):
    try:
        username = getpass.getuser()
        file_path = f"/home/{username}/game_engine_new/Asset/Asset.list"
        
        # Читаем текущее содержимое
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
        
        # Определяем следующий индекс
        last_index = max([int(line.split(' = ')[0]) for line in lines if line.split(' = ')[0].isdigit()], default=-1)
        new_index = last_index + 1
        
        # Формируем новую запись
        new_entry = f"{new_index} = {name_asset} = {directory_asset}\n"
        
        # Добавляем и сохраняем
        with open(file_path, 'a') as file:
            file.write(new_entry)
            
        return new_index
        
    except Exception as e:
        print(f"Ошибка при добавлении ассета: {e}")
        return None

def print_full_asset_list():

    username = getpass.getuser()
    asset_list = "/home/" + username + "/game_engine_new/Asset/Asset.list"

    with open(asset_list , "r") as file:
        Asset_list = file.read()

    print(Asset_list)
