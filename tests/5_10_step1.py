"""
Декоратор-повторитель
Напишите декоратор repeater, который трижды вызывает декорированную функцию

Ваша задача написать только определение функции декоратора repeater
"""


def repeater(func):
    def wrapper(*args):
        for i in range(3):
            func(*args)

    return wrapper


@repeater
def multiply(num1, num2):
    print(num1 * num2)


multiply(9, 4)


@repeater
def some_func(a, b, c):
    print(a ** b + c)


some_func(4, 5, 4)
some_func(14, 51, 34)
