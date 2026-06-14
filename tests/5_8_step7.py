"""
Функция make_repeater
Ваша задача создать функцию-замыкание make_repeater,
которая должна дублировать переданную в нее строку N раз.
При создании замыкания передается число N - количество для повторения.
"""


def make_repeater(start_value):
    def inner(income):
        return start_value * income

    return inner


repeat_5 = make_repeater(5)
print(repeat_5('Hello'))
print(repeat_5('World'))
