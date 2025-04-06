"""
Определите функцию overlapping, которая принимает два списка и возвращает True, если у них есть хотя бы один общий
элемент, в противном случае — False.

ВЫ можете решать задачу удобным для вас способом, но попробуйте реализовать с использованием функции is_member из
предыдущего шага.
"""


# def is_member(v, lst):
#    return v in lst


def overlapping(s1, s2):
    for el in s1:
        if el in s2:
            return True
        else:
            continue
    return False
