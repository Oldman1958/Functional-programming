"""
Напишите функцию convert_to, которая имеет следующие параметры:

    — values - список однотипных элементов. Элементы могут быть типа float, int, str

    — type_to - необязательный параметр, по умолчанию принимает тип int

Функция convert_to должна конвертировать все элементы списка values в тип type_to
и возвращать новый список в качестве результата.
Используйте функцию map для конвертирования элементов
"""


def convert_to(values, type_to=int):
    return [type_to(x) for x in values]


numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150]
print(convert_to(numbers, str))

numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150]
print(convert_to(numbers, float))

numbers = ['-383', '-101', '121', '40', '278', '118', '-462']
print(convert_to(numbers))

numbers = ['-383', '-101', '121', '40', '278', '118', '-462']
print(convert_to(numbers, float))
