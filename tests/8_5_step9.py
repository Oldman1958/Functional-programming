""" 
Рефакторинг генератора
Перед вами генератор flatten_matrix, который обходит все элементы двумерного списка 
и возвращает их по одному.

По сути, преобразование результата работы flatten_matrix в список 
позволяет создать одномерный (плоский) список из двумерного списка.

Ваша задача — переписать генератор flatten_matrix через инструкцию yield from так, 
чтобы функциональность генератора при этом не пострадала. 

Гарантируется, что в генератор flatten_matrix будет поступать только двумерный список.


def flatten_matrix(nested_list):
    for sublist in nested_list:
        for item in sublist:
            yield item
"""


def flatten_matrix(nested_list):
    for sublist in nested_list:
        yield from sublist


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(flatten_matrix(nested_list)))
