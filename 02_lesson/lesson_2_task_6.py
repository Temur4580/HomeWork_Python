# lesson_2_task_6.py
# Фильтрация списка

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

print("Элементы, которые меньше 30 и делятся на 3 без остатка:")

for number in lst:
    if number < 30 and number % 3 == 0:
        print(number)
