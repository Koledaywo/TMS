# Напишите функцию get_longest_word, которая на вход принимает текст
# (только английские слова и пробелы), и возвращает самое длинное слово из этого текста.
# Для разбиения строки на слова используйте функцию split.
def get_longest_word(text: str) -> str:
    # разбитие текста на слова
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word #самое длинное слово в тексте


text = input("Введите свой текст: ")
longest_word = get_longest_word(text)
print("Самое длинное слово:", longest_word)
