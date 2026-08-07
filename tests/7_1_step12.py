"""
Перепишите рекурсивную функцию speller так,
чтобы она выводила буквы слова в обратном порядке (каждую букву на новой строке)
"""


def speller(word):
    if len(word) > 0:
        # так было
        # print(word[0], end=' ')
        speller(word[1:])
        # так стало
        print(word[0], end='\n')

speller('Artem')
speller('Egorov')
