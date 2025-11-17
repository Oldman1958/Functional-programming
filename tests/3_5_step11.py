"""
Чистый lstrip
Напишите функцию lstrip, которая принимает список lst и значение value.
Функция lstrip должна теперь создать новый список, который является копией lst, но без элементов в самом начале,
равных значению value. Изначальный список, переданный в lst, не должен измениться
"""


def lstrip(lst, value):
    lst_new = lst.copy()
    while lst_new and lst_new[0] == value:
        lst_new.pop(0)
    return lst_new


data = [0, 0, 1, 0, 2, 3]
print(data)
print(lstrip(data, 0))
print(data)
