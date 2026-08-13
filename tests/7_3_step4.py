"""
Возведение в степень
Перед вами функция power, которая при помощи итерации возводит параметр a в степень n

def power(a: int, n: int) -> int:
    total = 1
    for i in range(n):
        total *= a
    return total


Перепишите реализацию функции power с итерации на рекурсию.
Названии функции и параметры не должны меняться
"""


def power(a: int, n: int) -> int:
    if n == 0: return 1
    if n == 1: return a
    return a * power(a, n - 1)


print(power(2, 3))
