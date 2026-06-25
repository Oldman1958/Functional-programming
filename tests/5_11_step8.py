"""
Декоратор limit_query
Напишите декоратор limit_query, который ограничивает вызов оригинальной функции так,
чтобы она могла вызываться не больше трех раз.
Когда декорируемая функция исчерпает лимит вызовов, необходимо выводить на экран фразу

 «Лимит вызовов закончен, все 3 попытки израсходованы»

Если лимит исчерпан, оригинальная функция не должна быть вызвана, декоратор возвращает None
"""

from functools import wraps

def limit_query(func):
    counter = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        wrapper.total_calls = counter
        if counter <= 3:
            res = func(*args, **kwargs)
            return res
        else:
            print("Лимит вызовов закончен, все 3 попытки израсходованы")
            return None

    wrapper.total_calls = 0
    return wrapper

@limit_query
def add(a: int, b: int):
    return a + b

print(add(4, 5))
print(add(5, 8))
print(add(9, 43))
print(add(10, 33))
print(add.__name__)



