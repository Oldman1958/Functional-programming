"""
Напишите функцию find_different_indexes, которая принимает две строки одинаковой длины
и возвращает список индексов, на позициях которых находятся разные символы в этих строках.
"""


def find_different_indexes(s1, s2):
    return [num for num, val in enumerate(s1) if s1[num] != s2[num]]


print(find_different_indexes('abcd', 'artd'))
print(find_different_indexes('abcd', 'abcd'))
print(find_different_indexes('abracadabra', 'uzrucuduzru'))
print(find_different_indexes('qwerty', 'asdfgh'))
