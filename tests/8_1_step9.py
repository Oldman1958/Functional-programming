""" 
Генератор нечетных чисел
Напишите генератор-функцию gen_odd, которая принимает натуральное число n 
и генерирует последовательность нечетных чисел от 1 до n включительно.
"""


def gen_odd(n):
    i = 1
    while i <= n:
        yield i
        i += 2


for value in gen_odd(5):
    print(value)

for value in gen_odd(10):
    print(value)

gen = gen_odd(6)
print(next(gen))
print(next(gen))
print(next(gen))
try:
    next(gen)
except StopIteration:
    print('Завершили обход генератора')
else:
    raise ValueError('Вы создали не генератор')
