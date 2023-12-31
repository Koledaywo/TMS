# Напишите функцию generate_natural_cubes(n), которая принимает число n и возвращает список,
# состоящий из кубов первых n натуральных чисел. То есть [1**3, 2**3, 3**3, ..., n**3].
# Обязательно использование генераторов списков.
def cubes_generate(n: int) -> list:
    return [i ** 3 for i in range(1, n + 1)]

n = int(input("Введите число: "))
# n (int): Количество натуральных чисел для генерации кубов

cubes_list = cubes_generate(n)
# list: Список кубов первых n натуральных чисел

print(f"Кубы первых {n} натуральных чисел: {cubes_list}")
