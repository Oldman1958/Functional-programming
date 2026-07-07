"""
Декоратор multiply_result_by
Создайте декоратор multiply_result_by, который принимает аргумент N
и возвращает функцию-декоратор, которая умножает результат декорированной функции на N
"""


def multiply_result_by(n):
    def decorator(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return n * result

        return inner

    return decorator


@multiply_result_by(2)
def my_function(x, y):
    return x + y


print(my_function(5, 6))


@multiply_result_by(3)
@multiply_result_by(4)
def my_function(x, y):
    return x + y


print(my_function(2, 3))
