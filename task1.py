# Завдання 1
# Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії та сортує в піддиректорії, 
# назви яких базуються на розширенні файлів.

import os
import shutil
import argparse

# Рекурсивна функція для копіювання та сортування файлів
def copy_and_sort_files(src_dir, dest_dir):
    try:
        # Перебираємо всі файли та піддиректорії у вихідній директорії
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                # Отримуємо шлях до файлу
                file_path = os.path.join(root, file)
                
                # Отримуємо розширення файлу
                file_extension = os.path.splitext(file)[1][1:]  # Наприклад, 'txt' або 'jpg'

                # Створюємо нову піддиректорію в директорії призначення на основі розширення файлу
                dest_subdir = os.path.join(dest_dir, file_extension)
                os.makedirs(dest_subdir, exist_ok=True)
                
                # Копіюємо файл у відповідну піддиректорію
                dest_file_path = os.path.join(dest_subdir, file)
                shutil.copy2(file_path, dest_file_path)
                print(f'Скопійовано {file_path} до {dest_file_path}')
                
    except Exception as e:
        print(f'Помилка під час копіювання файлів: {e}')


def main():
    # Налаштовуємо парсер аргументів командного рядка
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням.")
    parser.add_argument('src_dir', help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням dist)')

    # Зчитуємо аргументи
    args = parser.parse_args()

    # Перевіряємо, чи існує вихідна директорія
    if not os.path.isdir(args.src_dir):
        print(f'Вихідна директорія {args.src_dir} не існує.')
        return

    # Створюємо директорію призначення, якщо її немає
    os.makedirs(args.dest_dir, exist_ok=True)

    # Викликаємо функцію для рекурсивного копіювання та сортування
    copy_and_sort_files(args.src_dir, args.dest_dir)

if __name__ == '__main__':
    main()

# Приклад виклику:
# python task1.py "шлях_до_вихідної_директорії" "шлях_до_директорії_призначення"
# python task1.py "C:\Users\serhi\Downloads\Certificates" "C:\Users\serhi\Downloads\algo_dist"
# python task1.py "C:\Users\serhi\Downloads\Certificates"


