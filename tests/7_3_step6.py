"""

"""


def is_palindrome(word: str) -> bool:
    # Приводим слово к нижнему регистру и оставляем только буквы (на случай пробелов/знаков)
    cleaned = ''.join(ch.lower() for ch in word if ch.isalpha())

    # Базовый случай: пустая строка или один символ — это палиндром
    if len(cleaned) <= 1:
        return True

    # Если крайние символы не совпадают — не палиндром
    if cleaned[0] != cleaned[-1]:
        return False

    # Рекурсивный вызов для внутренней части строки
    return is_palindrome(cleaned[1:-1])


# Примеры использования:
print(is_palindrome('abba'))  # True
print(is_palindrome('Racecar'))  # True
print(is_palindrome('Qwerty'))  # False
