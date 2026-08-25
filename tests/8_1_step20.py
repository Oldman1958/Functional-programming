""" 
Функция range - 3
Теперь ваша задача создать полную копию встроенного объекта range. 
Он может быть вызван от одного, двух или трех аргументов.

Если вызов происходит от одного аргумента n, 
то my_range_gen  генерирует все числа от 0 до n не включительно.
 
Если вызов происходит от двух аргументов a и b, 
то my_range_gen  генерирует все числа от a включительно до b не включительно.
 
Если вызов происходит от трех аргументов a , b и step, 
то my_range_gen  генерирует все числа от a включительно до b не включительно 
c шагом step( может быть отрицательное значение).
"""


def my_range_gen(*args):
    
    # Распаковка аргументов в start, stop, step
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    else:  # len(args) == 3
        start, stop, step = args

    # Генерация значений с учётом направления шага
    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step


for i in my_range_gen(5):
    print(i)
for i in my_range_gen(10, 20):
    print(i)
for i in my_range_gen(10, 30, 3):
    print(i)
