""" 
Число-палиндром
Ваша задача — создать сопрограмму is_palindrome, 
которая проверяет поступающее ей натуральное число на палиндром.

Числа поступают в сопрограмму при помощи метода send. 
Сопрограмма должна порождать значение True, если число одинаково можно записать слева направо 
и справа налево, в противном случае - значение False. 

Вам необходимо написать только определение функции-сопрограммы is_palindrome.
"""


def is_palindrome():
    num = yield
    while True:
        num = yield str(num) == str(num)[::-1]




coro = is_palindrome()
next(coro)
print(coro.send(1771))
print(coro.send(987))
print(coro.send(1))
print(coro.send(1234321))

"""coro = is_palindrome()
next(coro)
for num in [1, 12, 123, 1221, 45654, 999]:
    print(coro.send(num))"""
