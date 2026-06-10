"""
Напишите функцию calculate_high_low_avg,
которая принимает произвольное количество позиционных аргументов в виде целых чисел.
Функция находит среднее арифметическое самого большого и самого маленького из аргументов и возвращает в качестве ответа.

К тому же, если в calculate_high_low_avg передать необязательный именованный аргумент log_to_console со значением True,
то дополнительно функция должна вывести на экран информацию в следующем формате:

high={max}, low={min}, avg={average}

где max - принимает значение самого большого аргумента, min - принимает значение самого маленького аргумента,
average - принимает среднее арифметическое самого большого и самого маленького из аргументов.
Напомню, что return сразу же производит выход из функции.
"""


def calculate_high_low_avg(*args, log_to_console=False):
    result = (min(args) + max(args)) / 2
    if log_to_console:
        print(f"high={max(args)}, low={min(args)}, avg={result}")
        return result
    return result


avg = calculate_high_low_avg(1, 2, 3, 4, 5)
print(avg)

avg = calculate_high_low_avg(1, 2, 3, 4, 5, log_to_console=True)
print(avg)
