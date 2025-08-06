def print_hundred_table():
    table = [[i + j * 10 for i in range(1, 11)] for j in range(25)]
    
    # Печатаем саму таблицу
    for row in table:
        # Форматируем каждое число с выравниванием по правому краю (3 символа)
        print(" | " + " | ".join(f"{num:3}" for num in row) + " | ")
    
    
    input("\n\nчтобы выйти нажмите Enter")

# Вызываем функцию
print_hundred_table()