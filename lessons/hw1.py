#Вывести на экран числа кратные 5 от 0 до 100 включительно.

# Сделать это с помощью функции range с шагом 5
for i in range(0, 101, 5):
    print(i)

# Сделать это с помощью функции range c шагом 1 и вложенным if
for i in range(101):
    if i % 5 == 0:
        print(i)
#Программа выводит на экран числа от 0 до 100.
# После вывода каждого числа спрашивайте у пользователя “Should we break?”.
# Если он ответил “yes” - завершите программу.
# Иначе - продолжайте вывод чисел.

for i in range(101):
    print(i)
    users_answer = input("Should we break? (yes/no): ")
    if users_answer.lower() == "yes":
        break


# Сделайте предыдущую задачу, добавив проверку на корректность ответа пользователя.
# Если он ответил “yes” - завершите программу.
# Если он ответил “no” - продолжайте - продолжайте вывод чисел.
# Если что-то другое - напечатайте "Don't understand you" и продолжайте спрашивать до тех пор,
# пока ответ не будет корректным.

for i in range(101):
    print(i)
    while True:
        users_answer = input("Should we break? (yes/no): ").lower()
        if users_answer == "yes":
            break
        elif users_answer == "no":
            break
        else:
            print("Don't understand you. Please enter 'yes' or 'no'.")

    if users_answer == "yes":
        break
