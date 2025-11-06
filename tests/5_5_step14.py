"""
Ваша задача написать функцию count_strings, которая принимает произвольное количество аргументов.
Функция должна среди всех переданных значений найти только строки, найти их количество и  вернуть в качестве результата.
Ваша задача написать только определение функции count_strings
"""

def count_strings(*args):
    count = 0
    for i in args:
        if isinstance(i, str):
            count += 1
    return count

print(count_strings(1, 2, 'hello', True, 't'))

print(count_strings('1', '2', 'hello', True, 't'))

print(count_strings())
