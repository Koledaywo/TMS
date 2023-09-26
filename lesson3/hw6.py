# Пользователь вводит месяц и число. Выведите True, если такой день есть в году.
user_month = input("Введите месяц: ").lower()
user_day = int(input("Введите число: "))

# Проверяем, есть ли введенный день в году
days_in_month = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

if user_month in days_in_month and 1 <= user_day <= days_in_month[user_month]:
    print(True)
else:
    print(False)
