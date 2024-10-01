# Завдання 2
# Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови, 
# що користувач повинен мати можливість вказати рівень рекурсії.

import turtle

# Функція для малювання однієї сторони сніжинки Коха
def koch_curve(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_curve(length, depth - 1)
        turtle.left(60)
        koch_curve(length, depth - 1)
        turtle.right(120)
        koch_curve(length, depth - 1)
        turtle.left(60)
        koch_curve(length, depth - 1)

# Функція для малювання сніжинки Коха
def koch_snowflake(length, depth):
    for _ in range(3):
        koch_curve(length, depth)
        turtle.right(120)

def main():
    # Запитуємо рівень рекурсії у користувача
    depth = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

    # Налаштування екрану turtle
    turtle.speed(0)  # Максимальна швидкість малювання
    turtle.penup()
    turtle.goto(-150, 100)  # Позиціонуємо сніжинку на екрані
    turtle.pendown()

    # Малюємо сніжинку Коха
    koch_snowflake(300, depth)

    # Завершення малювання
    turtle.done()

if __name__ == '__main__':
    main()
