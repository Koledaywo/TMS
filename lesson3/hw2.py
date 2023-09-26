# Пользователь вводит число. Вывести True если чётное, иначе - False.

user_number = int(input("Введите число: "))

# Проверка на чётность
is_even = user_number % 2 == 0

print(is_even)