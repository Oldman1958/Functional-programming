"""
Фильтрация аргументов
Ваша задача создать два декоратора

    1️ filter_even, который фильтрует только позиционные аргументы.
    Среди всех переданных значений он оставляет только четные числа, False и коллекции,
    длина которых четная

    2️ delete_short, который фильтрует только именованные аргументы.
    Среди всех переданных значений он оставляет только те, имена которых более четырех символов
"""


def filter_even(func):
    def wrapper(*args, **kwargs):
        filtered_args = []

        for arg in args:
            # Оставляем чётные числа
            if isinstance(arg, int) and arg % 2 == 0:
                filtered_args.append(arg)
            # Оставляем False (но не True)
            elif arg is False:
                filtered_args.append(arg)
            # Оставляем коллекции с чётной длиной
            elif hasattr(arg, '__len__') and len(arg) % 2 == 0:
                filtered_args.append(arg)

        return func(*filtered_args, **kwargs)

    return wrapper


def delete_short(func):
    def wrapper(*args, **kwargs):
        filtered_kwargs = {
            key: value
            for key, value in kwargs.items()
            if len(key) > 4
        }

        return func(*args, **filtered_kwargs)

    return wrapper


@delete_short
def info_kwargs(**kwargs):
    """Выводит информацию о переданных kwargs"""
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')


info_kwargs(first_name="John", last_name="Doe", age=33)


@filter_even
def concatenate(*args):
    result = ""
    for arg in args:
        result += arg
    return result


print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))


@filter_even
@delete_short
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate("Я", "хочу", "Выучить", "Питон", a="За", qwerty=10, c="Месяцев"))
