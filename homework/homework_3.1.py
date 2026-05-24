# 1. Запитуємо введення даних у користувача
try:
    num1 = float(input("Введіть перше число: "))
    operator = input("Введіть дію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    # 2. Обчислюємо результат залежно від оператора
    if operator == '+':
        result = num1 + num2
        print(f"Результат: {num1} + {num2} = {result}")

    elif operator == '-':
        result = num1 - num2
        print(f"Результат: {num1} - {num2} = {result}")

    elif operator == '*':
        result = num1 * num2
        print(f"Результат: {num1} * {num2} = {result}")

    elif operator == '/':
        # Перевірка на ділення на нуль
        if num2 == 0:
            print("Помилка: Ділити на нуль не можна!")
        else:
            result = num1 / num2
            print(f"Результат: {num1} / {num2} = {result}")

    else:
        print("Помилка: Невідома операція! Використовуйте лише +, -, * або /.")

except ValueError:
    print("Помилка: Будь ласка, вводьте тільки числа!")