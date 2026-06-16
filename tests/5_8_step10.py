"""
Обратный отсчет
Напишите функцию-замыкание countdown, которая будет вести обратный отсчёт
от переданного числа N до нуля.
После того как замыкание будет вызвано более N раз,
необходимо выводить сообщение «Превышен лимит, вы вызвали более N раз»
"""


def countdown(n):
    total = n
    def inner():
        nonlocal total, n
        if total > 0:
            print(total)
            total -= 1

        else:
            print(f"Превышен лимит, вы вызвали более {n} раз")
        return total

    return inner


count = countdown(3)
count()
count()
count()
count()
count()

a = countdown(2)
b = countdown(2)
a()
b()
b()
b()
a()
a()