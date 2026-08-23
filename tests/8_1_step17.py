""" 
Напишите функцию-генератор my_enumerate, 
которая копирует работу встроенной функции enumerate.
"""


def my_enumerate(v, start=0):
    index = start
    for i in v:
        yield index, i
        index += 1


lessons = ["Что такое функция", "Возвращаемое значение",
           "Параметры и аргументы функции",
           "Чистая функция", "Параметр *args"]

for i, lesson in my_enumerate(lessons):
    print("Урок {}: {}".format(i, lesson))
