""" 
Нахождение самого большого элемента списка
Напишите функцию get_max_recursive, которая принимает на вход вложенный список, 
конечными элементами которого являются целые числа, 
и возвращает самый большой элемент переданного списка. 
Уровень вложенности исходного списка произвольный. 

Ваша задача только написать определение рекурсивной функции get_max_recursive
"""


def get_max_recursive(lst):
    # самое маленькое число в Python - float('-inf')
    max_val = float('-inf')

    for item in lst:
        if isinstance(item, list):
            # Рекурсивный вызов для вложенного списка
            current_max = get_max_recursive(item)
        else:
            # Базовый случай: элемент — целое число
            current_max = item

        if current_max > max_val:
            max_val = current_max

    return max_val


print(get_max_recursive([1, 2, 3, 4, 5]))
print(get_max_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
print(get_max_recursive([1, 2, 3, 4, [[5]], [5]]))
