"""
Чиним баги Кузьмы - 2
Теперь убедитесь, что декоратор Кузьмы из предыдущего задания успешно работает и с другими функциями,
вне зависимости от количества аргументов и их типов.

Для решения задачи вам необходимо написать только определение функции-декоратора decorator.
"""


def decorator(func):
    def wrapper(*args, **kwargs):  # Добавили произвольное количество позиционных аргументов
        print('---Start calculation---')
        result = func(*args, **kwargs)  # Добавили произвольное количество позиционных аргументов
        print(f'---Finish calculation. Result is {result}---')
        return result

    return wrapper


@decorator
def add(*values):
    return sum(values)


add(1, 4, 5, 6)


@decorator
def add_with_factor(*values, factor=1):
    return sum(values) * factor


add_with_factor(1, 4, 5, 6, factor=2)
