"""
Напишите функцию is_only_one_positive, которая принимает произвольное количество числовых аргументов и возвращает True,
когда из всех переданных значений только одно положительное, в противном случае верните False

Вам необходимо написать только определение функции is_only_one_positive
"""


def is_only_one_positive(*args):
    count_positive = 0
    for i in args:
        if i > 0:
            count_positive += 1
    return True if count_positive == 1 else False


print(is_only_one_positive(-1, 2))
print(is_only_one_positive(-1, -2, -3, -4))
