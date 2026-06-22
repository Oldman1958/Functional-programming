"""
Валидация args
Напишите декоратор validate_all_args_str, который проверяет на корректность (валидирует)
переданные позиционные аргументы.
Корректным он считает любое строковое значение, стоящее в позиционном аргументе;
ключевые аргументы при проверке игнорируются.
Если было передано хотя бы одно не строковое значение в позиционный аргумент,
функция-декоратор validate_all_args_str должна

вывести на экран фразу «Все аргументы должны быть строками»;

вернуть None и не запускать оригинальную  функцию
Если же все аргументы корректны, validate_all_args_str запускает оригинальную функцию
со всеми переданными значениями.
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


@validate_all_args_str
def concatenate(*args):
    result = ""
    for arg in args:
        result += arg
    return result


print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))


@validate_all_args_str
def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += str(arg)
    return result


print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))


@validate_all_args_str
def concatenate(*args):
    result = ""
    for arg in args:
        result += arg
    return result


print(concatenate("Через", 9, "Месяцев"))
