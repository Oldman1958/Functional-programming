"""
Декоратор add_attrs
Ваша задача написать параметризированный декоратор add_attrs,
который принимает произвольное количество именованных аргументов
и на их основании добавляет новые атрибуты для оригинальной функции
"""

from functools import wraps


def add_attrs(**attrs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        # Добавляем атрибуты к обёртке
        # они будут доступны через декорированную функцию
        for name, value in attrs.items():
            setattr(wrapper, name, value)

        return wrapper

    return decorator


@add_attrs(test=True, ordered=True)
def add(a, b):
    return a + b


print(add(10, 5))
print(add.test)
print(add.ordered)


@add_attrs(hello='World', marks=[1, 2, 3], cash=100)
def add(a, b):
    return a + b


print(add(10, 5))
print(add.hello)
print(add.marks)
print(add.cash)
print(getattr(add, 'ordered', None))
