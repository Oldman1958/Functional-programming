"""
Замыкание-аккумулятор 2
На предыдущем шаге мы реализовали функцию-замыкание create_accumulator, которая накапливала сумму,
начиная с нуля.
Давайте ее усовершенствуем, чтобы она могла начинать суммировать, начиная с определенного значения.
Это значение мы ей будем передавать, но оно является необязательным.
Посмотрите пример ниже:

summator_1 = create_accumulator(100)
print(summator_1(1)) # печатает 101
print(summator_1(5)) # печатает 106
print(summator_1(2)) # печатает 108

summator_2 = create_accumulator()
print(summator_2(3)) # печатает 3
print(summator_2(4)) # печатает 7


Во втором примере мы не передали значение и значит сумма по умолчанию должна считаться с нуля.

Необходимо только определить функцию-замыкание create_accumulator, остальное мы сделаем за вас
"""


def create_accumulator(start_value=0):
    total = start_value

    def accumulator(value):
        nonlocal total
        total += value
        return total

    return accumulator


summator_1 = create_accumulator(100)
print(summator_1(1))  # печатает 101
print(summator_1(5))  # печатает 106
print(summator_1(2))  # печатает 108

summator_2 = create_accumulator()
print(summator_2(3))  # печатает 3
print(summator_2(4))  # печатает 7
