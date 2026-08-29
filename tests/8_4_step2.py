"""
Ниже представлен код из урока, где мы разбирали различные состояния генератора. 
При запуске данного кода возникает исключение 
и из-за него не отрабатывает последняя строка.
Ваша задача - обработать возникающее исключение так, 
чтобы все оставшиеся строки смогли отработать без ошибок.
"""

from inspect import getgeneratorstate


def my_coro(a):
    print(f'Запускаем корутину со значением a={a}')
    b = yield a
    print(f'Получено значение b={b}')
    c = yield a + b
    print(f'Получено значение c={c}')


coro = my_coro(7)
print(getgeneratorstate(coro))
next(coro)
# Код далее обернуть в try - except с обработкой исключения getgeneratorstate
try:
    print(getgeneratorstate(coro))
    print(coro.send(23))
    print(getgeneratorstate(coro))
    print(coro.send(100))
except StopIteration:
    print(getgeneratorstate(coro))
