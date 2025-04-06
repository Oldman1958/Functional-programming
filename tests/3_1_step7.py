"""
Напишите функцию is_leap, которая проверяет является ли переданный год високосным или нет.

Год является високосным, если он соответствует следующим правилам:

Годы, делящиеся на 100 без остатка, не являются високосными, за исключением годов, которые делятся на 400 без остатка.
Например, 1900 год не является високосным, а 2000 год — является.
Годы делящиеся на 4 без остатка (например, 2016, 2024), являются високосными.
Напишите только определение функции is_leap
"""


def is_leap(year):
    return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False

print(is_leap(2004))
