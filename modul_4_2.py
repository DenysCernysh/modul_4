def get_cats_info(path):
    cats_info = []  # Створюємо пустий список для зберігання інформації про котів

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')  # Розділяємо рядок за комами
                if len(cat_data) == 3:  # Перевіряємо, чи кількість елементів у рядку дорівнює 3
                    # Створюємо словник з інформацією про кота та додаємо його до списку
                    cat_info = {"id": cat_data[0], "name": cat_data[1], "age": cat_data[2]}
                    cats_info.append(cat_info)
                else:
                    print(f"Issue with line: {line}")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Повертаємо список інформації про котів
    return cats_info

# Викликаємо функцію get_cats_info з шляхом до файлу
cats_info = get_cats_info("C:\\Users\\user\\Desktop\\goit\\modul_4\\Path.txt")
print(cats_info)
