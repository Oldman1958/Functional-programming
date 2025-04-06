"""
Напишите функцию find_longest_word_len, которая принимает список слов и возвращает длину самого длинного из них.
"""


def find_longest_word_len(s):
    a = []
    for i in s:
        a.append(len(i))
    return max(a)

