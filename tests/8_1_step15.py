""" 
Генератор факториалов
Напишите генератор-функцию gen_factorial, которая принимает натуральное число n 
и генерирует факториалы чисел от 1! до n!
"""


def gen_factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result

for value in gen_factorial(5):
    print(value)
