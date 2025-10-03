"""
Напишите lambda функцию, которая принимает произвольное количество числовых аргументов и выводит
их среднее арифметическое.
Для проверки решения присвойте вашу lambda функцию переменной average.

Вводить и выводить ничего не нужно, только определить переменную average
"""

average = lambda *args: sum(args) / len(args)

print(average.__name__)
print(average(4, 5, 6))
print(average(2, 6))
print(average.__name__)
print(average(10, 6, 5, 4, 3, 7, 9, 15))
