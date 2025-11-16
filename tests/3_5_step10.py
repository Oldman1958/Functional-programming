"""
Нечистый lstrip
Напишите функцию lstrip, которая принимает список lst и значение value.
Функция lstrip должна удалить из начала списка lst все упоминания значения value,
остальные элементы должны остаться без изменения, даже те, которые равны значению value, но не находятся в начале списка.

Изначальный список lst должен измениться после вызова lstrip. Сама lstrip ничего не возвращает
"""


def lstrip(lst, value):
    while lst and lst[0] == value:
        lst.pop(0)


data = [0, 0, 1, 0, 2, 3]
print(data)
print(lstrip(data, 0))
print(data)

data = [0, 0, 0, 1, 0, 2, 3, 0, 0]
print(data)
print(lstrip(data, 0))
print(data)

