# Завдання 3 (необов'язкове завдання). Ханойські башти
# Напишіть програму, яка виконує переміщення дисків з стрижня А на стрижень С, використовуючи стрижень В як допоміжний. 
# Диски мають різний розмір і розміщені на початковому стрижні у порядку зменшення розміру зверху вниз.

def hanoi_tower(n, source, target, auxiliary, state):
    if n == 1:
        # Переміщуємо один диск безпосередньо
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
    else:
        # Рекурсивно переміщуємо n-1 дисків на допоміжний стрижень
        hanoi_tower(n - 1, source, auxiliary, target, state)
        
        # Переміщуємо найбільший диск безпосередньо
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
        
        # Рекурсивно переміщуємо n-1 дисків з допоміжного стрижня на цільовий
        hanoi_tower(n - 1, auxiliary, target, source, state)

def main():
    # Вхід: кількість дисків
    n = int(input("Введіть кількість дисків: "))

    # Початковий стан: всі диски на стрижні A
    state = {
        'A': list(range(n, 0, -1)),  # Диски у порядку від найбільшого до найменшого
        'B': [],
        'C': []
    }

    print(f"Початковий стан: {state}")

    # Викликаємо функцію для рішення задачі
    hanoi_tower(n, 'A', 'C', 'B', state)

    print(f"Кінцевий стан: {state}")

if __name__ == "__main__":
    main()
