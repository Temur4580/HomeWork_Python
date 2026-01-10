import math

def square(side):
    area = side * side
    if isinstance(side, int):
        return area
    else:
        return math.ceil(area)

print("Результаты:")
print("square(5) =", square(5))
print("square(3.5) =", square(3.5))
print("square(4) =", square(4))
