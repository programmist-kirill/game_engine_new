import os

def get_asset_and_directory_parameter(filename):
    # Путь к директории с файлами
    directory_path = "/home/kirill/game_engine_new/Data/Config/Asset/"
    file_path = os.path.join(directory_path, filename)

    asset_value = None
    directory_parameter = None

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Перебираем строки файла
        for line in lines:
            line = line.strip()
            # Ищем строку, содержащую 'asset' (непустая строка)
            if line and 'asset' in line:
                asset_value = line
            # Ищем строку, начинающуюся с 'parameter='
            if line.startswith('parameter='):
                # Получаем значение параметра после '='
                parameter_value = line[len('parameter='):].strip()
                # Проверяем, есть ли в следующей строке 'parameter='
                # или в текущей строке есть 'parameter=' с переносом строки
                # В данном случае, поскольку формат предполагает, что 'parameter=' может быть на отдельной строке,
                # ищем следующую строку, если есть
                # Но так как мы читаем все строки, можно искать сразу
                # В случае, если 'parameter=' идет на следующей строке, нужно обработать это
                # Для этого можно запомнить текущий индекс и проверить следующую строку
                # Однако, проще всего искать 'parameter=' в строках
                # В текущем контексте, поскольку мы уже нашли строку, начинающуюся с 'parameter=',
                # сохраняем значение
                # Если есть перенос строки, то он уже учтен при чтении файла
                # Поэтому, если после 'parameter=' есть перенос строки, то значение пустое
                # В противном случае, значение после '='
                # В случае, если значение пустое, то ищем следующую строку
                # Но в вашем формате, похоже, что значение после 'parameter=' может быть пустым
                # Поэтому, если значение пустое, ищем следующую строку
                if not parameter_value:
                    # Попытка получить значение из следующей строки
                    next_index = lines.index(line) + 1
                    if next_index < len(lines):
                        next_line = lines[next_index].strip()
                        if next_line:
                            parameter_value = next_line
                # После получения значения, проверяем, содержит ли оно 'directory_parameter'
                if 'directory_parameter' in parameter_value:
                    directory_parameter = parameter_value
    except FileNotFoundError:
        print(f"Файл {filename} не найден в директории {directory_path}.")
        return None

    # Формируем результат в виде словаря
    result = {
        'asset': asset_value,
        'directory_parameter': directory_parameter
    }
    return result

# Пример использования:
filename = 'linia.asset'
result = get_asset_and_directory_parameter(filename)
print(result)