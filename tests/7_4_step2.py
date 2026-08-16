""" 
Сумма списка
Напишите функцию sum_recursive, которая принимает на вход вложенный список, 
конечными элементами которого являются целые числа, 
и возвращает сумму элементов переданного списка. Уровень вложенности списка произвольный.

Ваша задача только написать определение рекурсивной функции sum_recursive
"""


def sum_recursive(lst):
    total = 0
    for value in lst:
        # проверяем тип элемента
        if isinstance(value, list):
            # если это список, то
            # вызываем рекурсивный шаг для
            # нахождения суммы его элементов
            sum_nested = sum_recursive(value)
            total += sum_nested
        else:
            # Если это число, то сразу добавляем к total
            total += value

    return total


print(sum_recursive([1, 2, 3, 4, 5]))
print(sum_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
print(sum_recursive([1, 2, 3, 4, [[5]], [5]]))
