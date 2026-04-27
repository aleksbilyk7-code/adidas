# Завдання 1: Квадрат числа
print("--- Завдання 1 ---")
number = float(input("Введіть число: "))
print(f"Квадрат числа: {number**2}\n")

# Завдання 2: Середнє трьох чисел
print("--- Завдання 2 ---")
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))
print(f"Середнє: {(num1 + num2 + num3) / 3}\n")

# Завдання 3: Перетворення хвилин у години
print("--- Завдання 3 ---")
total_minutes = int(input("Введіть кількість хвилин: "))
print(f"{total_minutes // 60} години {total_minutes % 60} хвилин\n")

# Завдання 4: Розрахунок знижки
print("--- Завдання 4 ---")
price = float(input("Введіть ціну: "))
discount = float(input("Введіть знижку (%): "))
print(f"Ціна зі знижкою: {price * (1 - discount / 100)}\n")

# Завдання 5: Остання цифра числа
print("--- Завдання 5 ---")
num_last = int(input("Введіть ціле число: "))
print(f"Остання цифра: {num_last % 10}\n")

# Завдання 6: Периметр прямокутника
print("--- Завдання 6 ---")
length = float(input("Введіть довжину: "))
width = float(input("Введіть ширину: "))
print(f"Периметр: {2 * (length + width)}\n")

# Завдання 7: Виведення числа в стовпчик
print("--- Завдання 7 ---")
number4 = int(input("Введіть 4-х значне число: "))
print(number4 // 1000)
print((number4 // 100) % 10)
print((number4 // 10) % 10)
print(number4 % 10)
