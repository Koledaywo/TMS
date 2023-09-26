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
