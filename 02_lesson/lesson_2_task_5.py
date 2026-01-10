# lesson_2_task_5.py
# Функция определения сезона по номеру месяца

def month_to_season(month):
    """Возвращает сезон года для указанного месяца"""
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Некорректный месяц"


# Пример использования
print("month_to_season(2) →", month_to_season(2))

# Дополнительные примеры
print("\nВсе месяцы:")
for m in range(1, 13):
    print(f"Месяц {m:2} → {month_to_season(m)}")