"""
Напишите функцию is_strings_equal, которая принимает две строки в качестве аргументов и сравнивает их между собой.

Строки считаются равными, если они имеют одинаковую длину и одинаковые символы в равном количестве вне зависимости от их
расположения.

Функция is_strings_equal должна вернуть True, если строки равны, в противном случае - False.
"""


def is_strings_equal(s1, s2):
    q1 = s1.sort
    q2 = s2.sort
    if q1 == q2:
        return True
    else:
        return False
