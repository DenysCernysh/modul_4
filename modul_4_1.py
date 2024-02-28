def total_salary(path):  # Визначення функції total_salary з одним аргументом path
    total = 0  # Ініціалізація змінної total як нуль
    count = 0  # Ініціалізація змінної count як нуль

    try:  # Початок блоку try-except для обробки винятків
        with open(path, 'r', encoding='utf-8') as file:  # Відкриття файлу за шляхом path для читання
            for line in file:  # Ітерація по кожному рядку у файлі
                data = line.strip().split(',')  # Розділення рядка на дані за комою
                print(data)
                if len(data) == 2:  # Перевірка, чи є два елементи у списку даних
                    salary = float(data[1])  # Конвертування другого елементу у ціле число
                    total += salary  # Додавання зарплати до загальної суми
                    count += 1  # Збільшення лічильника на 1
                else:
                    print(f"Ignoring invalid data: {line}")  # Виведення повідомлення про ігнорування недійсних даних

    except FileNotFoundError:  # Обробка винятку, якщо файл не знайдено
        print("File not found.")  # Виведення повідомлення про відсутність файлу
        return None, None  # Повернення кортежу з двома значеннями None
    except Exception as e:  # Обробка будь-якого іншого винятку
        print(f"An error occurred: {e}")  # Виведення повідомлення про помилку
        return None, None  # Повернення кортежу з двома значеннями None

    if count == 0:  # Перевірка, чи лічильник дорівнює нулю
        return 0, 0  # Повернення кортежу з двома нулями

    average = total / count  # Обчислення середньої зарплати
    return total, average  # Повернення кортежу з загальною сумою та середньою зарплатою

# Приклад використання функції
total, average = total_salary("C:\\Users\\user\\Desktop\\goit\\modul_4\\zp.txt")  # Виклик функції total_salary з шляхом до файлу
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")  # Виведення результатів на екран