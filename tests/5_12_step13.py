"""
Декоратор compose
Ваша задача написать параметризированный декоратор compose,
который принимает произвольное количество функций
и применяет их последовательно к результату декорируемой функции.
"""

from functools import wraps


def compose(*funks):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for fn in funks:
                result = fn(result)
            return result

        return wrapper

    return decorator


def double_it(a):
    return a * 2


def increment(a):
    return a + 1


@compose(double_it, increment)
def get_sum(*args):
    return sum(args)


print(get_sum(5))
print(get_sum(20, 10))
print(get_sum(5, 15, 25))


def double_it(a):
    return a * 2


def increment(a):
    return a + 1


@compose(increment, increment, double_it)
def get_sum(*args):
    return sum(args)


print(get_sum(5))
print(get_sum(20, 10))
print(get_sum(5, 15, 25))
