""" 
Генератор факториалов - 2
Измените генератор-функцию gen_factorial так, 
чтобы он стал выдавать бесконечную последовательность факториалов
"""


def gen_factorial():
    result = 1
    i = 1
    while True:
        result *= i
        yield result
        i += 1


count = 1
for value in gen_factorial():
    print(value)
    count += 1
    if count > 10:
        break
