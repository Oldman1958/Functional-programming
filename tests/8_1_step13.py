""" 
Генератор бесконечной арифметической прогрессии
Ваша задача создать функцию-генератор gen_arithmetic_progression, 
которая при вызове принимает два значения:

первый элемент прогрессии 
разность элементов прогрессии
Функция-генератор gen_arithmetic_progression должна выдавать элементы 
бесконечной арифметической прогрессии с учетом переданных значений

Ваша задача написать только определение функции-генератора gen_arithmetic_progression
"""


def gen_arithmetic_progression(start, step):
    elem = start
    while True:
        yield elem
        elem += step
        

count = 1
for value in gen_arithmetic_progression(5, 7):
    print(value)
    count += 1
    if count > 5:
        break


count = 8
for value in gen_arithmetic_progression(105, -5):
    print(value)
    count -= 1
    if count == 0:
        break
