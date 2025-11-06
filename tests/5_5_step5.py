"""
Напишите функцию create_attrs, которая принимает объект obj и список кортежей.
Каждый кортеж состоит из пары значений: имя атрибута в виде строки и его будущее значение.

Задача функции create_attrs — создать на основании внутренних кортежей списка новые атрибуты к переданному объекту.

Для проверки работоспособности программы скопируйте реализацию функции check_exist_attrs из предыдущего задания
"""


def check_exist_attrs(obj, lst):
    res = {k: True if hasattr(obj, k) else False for k in lst}
    return res


def create_attrs(obj, tpl):
    for i in tpl:
        setattr(obj, i[0], i[1])


def print_goods(lst):
    pass


create_attrs(print_goods, [('house', 1), ('level', 3), ('cost', 1000000)])
print(print_goods.house)
print(print_goods.level)
print(print_goods.cost)


def print_goods(lst):
    pass


create_attrs(print_goods, [('is_working', False), ('days', 10), ('status', 'Not ready')])

print(check_exist_attrs(print_goods, ['sort', 'is_working', 'days', 'status', 'upper']))
