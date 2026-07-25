"""
Напишите функцию filter_words, которая принимает список строк и возвращает новый список,
который состоит из строк, длина которых четыре символа, или начинающихся на заглавную букву S.
"""


def filter_words(strings):
    return list(filter(lambda x: len(x) == 4 or x.startswith('S'), strings))


days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six',
        'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
print(filter_words(days))

words = ['scheme', 'hypnothize', 'exposure', 'Syndrome',
         'Save', 'speculate', 'cane', 'welfare', 'blame', 'core']
print(filter_words(words))
