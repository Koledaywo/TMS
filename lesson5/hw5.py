from collections import Counter


def most_frequent_word(text: str) -> str:

    words = text.split()
    # Используем Counter для подсчета частоты каждого слова
    word_counts = Counter(words)
    # Находим слово с наибольшей частотой
    most_frequent_word = max(word_counts, key=word_counts.get)
    return most_frequent_word


# Пример использования
text = input("Введите текст с английскими словами и пробелами: ")
most_frequent_word = most_frequent_word(text)
print("Самое часто встречающееся слово:", most_frequent_word)
