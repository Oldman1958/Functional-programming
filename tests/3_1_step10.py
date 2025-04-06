"""
Напишите функцию get_leap_years, которая принимает два года y1 и y2, причем y1 <= y2, и возвращает список, состоящий из
високосных лет в промежутке от y1 включительно до  y2 не включительно. Года должны располагаться в нем в хронологическом
порядке.

При реализации функции get_leap_years, используйте ранее созданную функцию is_leap
"""


def is_leap(year):
    return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False


def get_leap_years(y1, y2):
    # count = 0
    out = []
    for i in range(y1, y2):
        if is_leap(i):
            out.append(i)
    return out

