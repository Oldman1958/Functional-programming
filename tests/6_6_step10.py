"""
Напишите функцию get_words_with_position,
которая принимает на вход строку words, состоящую из слов, разделенных пробелом.

Функция get_words_with_position должна создать и вернуть список кортежей,
где каждый элемент-кортеж должен содержать два значения:
само слово и его порядковый номер в исходной строке words.

Порядковый номер слов необходимо считать с единицы.

К примеру, такой вызов функции get_words_with_position

get_words_with_position('variation random electronics competence collapse')

должен вернуть следующий результат

[
 ('variation', 1),
 ('random', 2),
 ('electronics', 3),
 ('competence', 4),
 ('collapse', 5)
]

Ваша задача - написать реализацию функции get_words_with_position.
"""


def get_words_with_position(lst):
    return [(val, i) for i, val in enumerate(lst.split(), start=1)]


print(get_words_with_position('Куда ты тянешь свои ручки'))
print(get_words_with_position('И тянутся города Я в каждом из них бывал'))
