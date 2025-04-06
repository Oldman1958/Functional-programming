"""
Определите функцию print_histogram, которая принимает список целых чисел и выводит гистограмму на экран.

Например, вызов

print_histogram([4, 9, 6])

должен вывести на экран следующее:

****
*********
******
Ваша задача написать только определение функции print_histogram
"""


def print_histogram(s):
    for i in range(len(s)):
        print('*' * s[i])


print_histogram([4, 9, 6])
