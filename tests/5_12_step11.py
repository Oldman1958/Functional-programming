"""
Декоратор convert_to
Напишите декоратор convert_to,
который позволяет автоматически преобразовать возвращаемое значение в указанный тип данных.
Функция-декоратор convert_to имеет обязательный параметр type_,
в который необходимо передать тип данных для дальнейшего преобразования.
"""

from functools import wraps


def convert_to(type_):
    """
        Декоратор для автоматического преобразования возвращаемого значения функции
        в указанный тип данных.

        :param type_: тип данных, в который нужно преобразовать результат (например, int, str, list)
        :return: декорированную функцию
        """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # Преобразуем результат в указанный тип
            return type_(result)

        return wrapper

    return decorator


@convert_to(int)
def add_values(a, b):
    return a + b


result = add_values(10, 20)
print(f"Результат: {result}, тип результата {type(result)}")


@convert_to(str)
def add_values(a, b):
    return a + b


result = add_values(10, 20)
print(f"Результат: {result}, тип результата {type(result)}")


@convert_to(list)
def add_values(a, b):
    return a + b


result = add_values('hello', 'world')
print(f"Результат: {result}, тип результата {type(result)}")
