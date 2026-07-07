"""
Декоратор limit_query с параметром
Ваша задача переписать декоратор limit_query так,
чтобы он ограничивал разрешенное количество вызовов оригинальной функции
по переданному параметру limit.
Когда декорируемая функция исчерпает лимит вызовов, необходимо выводить на экран фразу

 «Лимит вызовов закончен, все <limit> попытки израсходованы»

Если лимит исчерпан, оригинальная функция не должна быть вызвана, декоратор возвращает None.
"""

from functools import wraps


def limit_query(limit=1):
    def decorator(func):
        counter = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal counter
            counter += 1
            wrapper.total_calls = counter
            if counter <= limit:
                res = func(*args, **kwargs)
                return res
            else:
                print(f"Лимит вызовов закончен, все {limit} попытки израсходованы")
                return None

        wrapper.total_calls = 0
        return wrapper

    return decorator


@limit_query(3)
def add(a: int, b: int):
    return a + b


print(add(4, 5))
print(add(5, 8))
print(add(9, 43))
print(add(10, 33))
print(add.__name__)
