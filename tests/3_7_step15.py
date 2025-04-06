"""
Напишите функцию info_kwargs, которая принимает произвольное количество именованных аргументов.

Функция info_kwargs должна распечатать именованные аргументы (каждый на новой строке) в виде пар «ключ = значение»,
где ключи должны следовать в алфавитном порядке.

Вам необходимо написать только определение функции info_kwargs
"""

def info_kwargs(**kwargs):
    for key, val in sorted(kwargs.items()):
        print(f'{key}: {val}')

# print(info_kwargs(first_name="John", last_name="Doe", age=33))
