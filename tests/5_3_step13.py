"""
Помните задачу «Проверка на високосность»?

Ваша задача реализовать данную функцию при помощи lambda оператора

Полученную функцию сохраните в переменную is_leap
"""

is_leap = lambda year: True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False

print(is_leap(1900))
print(is_leap.__name__)

print(is_leap.__name__)
print(is_leap(2000))
