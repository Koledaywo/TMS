# Напишите функцию is_year_leap, которая принимает число (год)
# и возвращает True если год високосный (см. комментарий к слайда),
# False если нет.
def leap_year(year: int) -> bool:

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True #выведтся в консоль если год високосный
    else:
        return False #если год не високосный


year = int(input("Введите год: "))
#year (int): Год для проверки, является числовы

print(f"Год {year} високосный: {leap_year(year)}")
