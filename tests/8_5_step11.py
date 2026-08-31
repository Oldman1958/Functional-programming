""" 
Плоский список
Перепишите рекурсивную функцию flatten 
из задачи «Превращаем вложенный список в плоский» в рекурсивный генератор. 
Имя для генератора оставьте прежним flatten 
"""


def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            # Делегируем вложенность через yield from — он сам прогонит все значения из генератора
            yield from flatten(item)
        else:
            # Базовый случай: отдаём элемент по одному
            yield item


for element in flatten([1, [2], [3, [4]]]):
    print(element)
