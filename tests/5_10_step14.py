"""
Валидация kwargs.
Напишите декоратор validate_all_kwargs_int_pos,
который проверяет на корректность переданные именованные аргументы.
Корректным будет считаться именованный аргумент,
значение которого является целым положительным числом.
Позиционные аргументы игнорируются во время проверки декоратора validate_all_kwargs_int_pos.

Если было передано хотя бы одно некорректное значение в именованный аргумент,
функция-декоратор validate_all_kwargs_int_pos должна:

вывести на экран фразу «Все именованные аргументы должны быть положительными числами»;

вернуть None и не запускать оригинальную функцию.
Если же все аргументы корректны,
validate_all_kwargs_int_pos запускает оригинальную функцию со всеми переданными значениями.

Также для проверки вам необходимо скопировать из предыдущего шага
реализацию декоратора validate_all_args_str,
потому что в проверках будет использоваться валидация сразу и на *args, и на **kwargs.
"""


def validate_all_args_str(func):
    def wrapper(*args, **kwargs):
        for i in args:
            if not isinstance(i, str):
                print("Все аргументы должны быть строками")
                return None
            else:
                continue
        return func(*args, **kwargs)

    return wrapper


def validate_all_kwargs_int_pos(func):
    def wrapper(*args, **kwargs):
        for v in kwargs.values():
            if not isinstance(v, int) or int(v) <= 0:
                print("Все именованные аргументы должны быть положительными числами")
                return None
            else:
                continue
        return func(*args, **kwargs)

    return wrapper


@validate_all_kwargs_int_pos
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate(a="i", b='Love', c="Python"))


@validate_all_kwargs_int_pos
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate(a=10, b=20, c=50))


@validate_all_args_str
@validate_all_kwargs_int_pos
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate('Hello', 2, 'World', a="i", b='Love', c="Python"))
