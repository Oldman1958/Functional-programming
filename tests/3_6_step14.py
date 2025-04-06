"""
Напишите функцию check_sum, которая принимает произвольное количество аргументов типа int.

Данная функция должна вывести на экран фразу «not enough», если сумма всех элементов меньше 50,
в противном случае нужно вывести «verification passed»

Вам необходимо написать только определение функции check_sum
"""


def check_sum(*args):
    print('not enough' if sum(args) < 50 else 'verification passed')

check_sum(8, 11)
check_sum(10, 10, 10, 10, 9)
check_sum(20, 20, 10)
