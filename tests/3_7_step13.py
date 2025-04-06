"""
Напишите функцию concatenate(), которая принимает произвольное число именованных аргументов и объединяет их
в одну большую строку без разделителей.

Вам необходимо написать только определение функции concatenate

Обратите внимание, что передаваемые значения могут быть различных типов данных
"""


def concatenate(**kwargs):
    out = []
    for key in kwargs:
        out += str(kwargs[key])
    result = ''.join(out)
    return result


print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))
print(concatenate(first='i got ', second=5, third=" stars"))
