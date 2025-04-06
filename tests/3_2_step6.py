"""
Напишите функцию filter_long_words, которая принимает список слов и целое число N и возвращает список слов, длина
которых больше чем число N
"""


def filter_long_words(s, n):
    q = []
    for i in s:
        if len(i) > n:
            q.append(i)
    return q
