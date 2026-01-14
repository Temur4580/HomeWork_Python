from smartphone import Smartphone

# Создаем каталог (список) смартфонов
catalog = []

# Добавляем 5 разных экземпляров класса Smartphone
catalog.append(Smartphone("Apple", "iPhone 15", "+79111234567"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79229876543"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79333456789"))
catalog.append(Smartphone("Google", "Pixel 8", "+79444567890"))
catalog.append(Smartphone("OnePlus", "12", "+79555678901"))

# Выводим весь каталог в заданном формате
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
