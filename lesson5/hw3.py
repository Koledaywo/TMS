# Напишите функцию generate_squares, которая принимает произвольное количество
# аргументов и возвращает список, состоящий из их квадратов.
# То есть generate_squares(1, 2, 3) -> [1, 4, 9]

def generate_squares(*args):
    #args: Произвольное количество аргументов.

    return [x ** 2 for x in args]

numbers = input("Введите числа через пробел: ").split()
# Преобразуем введенные значения в целые числа
numbers = [int(num) for num in numbers]

# Вызываем функцию и выводим результат
squares_list = generate_squares(*numbers)
print("Квадраты аргументов:", squares_list)
