"""
Напишите функцию get_first_repeated_word, которая имеет один параметр words - список, состоящий из нескольких слов.
Функция должна найти первый элемент, который образует дубль с ранее стоящими элементами,
и вернуть его в качестве результата.
Если передан список, в котором все слова различны, функция get_first_repeated_word должна вернуть None
Регистр букв при сравнении нужно учитывать

Для функции  get_first_repeated_word  дополнительно нужно добавить

 1 док-строку  Находит первый дубль в списке

 2  аннотации при помощи модуля typing
"""
from typing import List, Optional


def get_first_repeated_word(words: List[str] = []) -> Optional[str]:
    '''Находит первый дубль в списке'''

    if len(words) != len(set(words)):
        temp_lst = []
        for word in words:
            if word not in temp_lst:
                temp_lst.append(word)
            else:
                return word
    return None

print(get_first_repeated_word(['ab', 'ca', 'bc', 'Ab', 'cA', 'aB', 'bc']))
print(get_first_repeated_word.__doc__)
print(get_first_repeated_word.__annotations__)
print(get_first_repeated_word(['hello', 'hi', 'hello']))

print(get_first_repeated_word(['ab', 'ca', 'bc', 'ab']))
