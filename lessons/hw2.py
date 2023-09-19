import random

# Программа загадывает случайное число от 0 до 100.
# Пользователь пытается угадать, вводя числа.
# Если пользователь угадал - выведите поздравление и завершите программу.
# Если пользователь не угадал, подскажите ему в в какую сторону идти. То есть,
# если число пользователя слишком большое - выведите “не угадал, число больше загаданного”.
# Если меньше - выведите “не угадал, число меньше загаданного”.
# рандомное  число от 0 до 100
random_int = random.randint(0, 100)

while True:
    user_int = int(input("Попробуйте угадать число от 0 до 100: "))

    if user_int == random_int:
        print("Поздравляем! Вы угадали число.")
        break
    elif user_int < random_int:
        print("Не угадал, число больше загаданного.")
    else:
        print("Не угадал, число меньше загаданного.")