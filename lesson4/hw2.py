#Программа выводит на экран числа от 0 до 100.
# После вывода каждого числа спрашивайте у пользователя “Should we break?”.
# Если он ответил “yes” - завершите программу.
# Иначе - продолжайте вывод чисел.

for i in range(101):
    print(i)
    users_answer = input("Should we break? (yes/no): ")
    if users_answer.lower() == "yes":
        break
