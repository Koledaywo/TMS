# Пользователь вводит одно число, сторона квардата.
# Вывести кортеж из трёх чисел: периметр квадрата, площадь квадрата, диагональ квадрата.

import math


def calculate_square_properties(side_length):
    # Периметр - 4 * сторона
    perimeter = 4 * side_length
    # Площадь - сторона * сторона
    area = side_length ** 2
    # Диагональ - сторона * sqrt(2)
    diagonal = side_length * math.sqrt(2)
    return (perimeter, area, diagonal)


# Получаем сторону квадрата от пользователя
side_length = float(input("Введите длину стороны квадрата: "))

# Рассчитываем периметр, площадь и диагональ
square_properties = calculate_square_properties(side_length)

# Выводим результат в виде кортежа
print("Периметр, площадь и диагональ квадрата:", square_properties)
