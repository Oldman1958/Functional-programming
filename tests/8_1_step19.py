""" 
Функция range - 2
Измените функцию-генератор my_range_gen так, 
чтобы она могла вызываться от одного или двух аргументов.

Если вызов происходит от одного аргумента n, 
то my_range_gen  генерирует все числа от 0 до n не включительно.

Если вызов происходит от двух аргументов a и b, 
то my_range_gen  генерирует все числа от a включительно до b не включительно.
"""


def my_range_gen(*args):
    if len(args) == 1:
        start, stop = 0, args[0]
    elif len(args) == 2:
        start, stop = args


    while start < stop:
        yield start
        start += 1

for value in my_range_gen(5):
    print(value)

for value in my_range_gen(3, 8):
    print(value)
