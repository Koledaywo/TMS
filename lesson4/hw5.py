#  Пользователь вводит произвольное число. Посчитайте сумму цифр этого числа используя операторы % и //
# Пример для числа 12.
# Ответ должен быть получен примерно так:
# answer = 12 % 10  # 2
# answer += 12 // 10  # 1
# print(answer)  # 3
number = int(input("Введите произвольное число: "))

sum_of_ints = 0

while number != 0:
    last_int = number % 10
    sum_of_ints += last_int

    number //= 10

print("Сумма цифр числа:", sum_of_ints)