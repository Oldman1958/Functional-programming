"""
Функция count_calls
В этом задании вам нужно сделать функцию-замыкание count_calls,
которая подсчитывает сколько раз она была вызвана.
Особенность этого замыкания заключается в том,
что количество вызовов должно храниться в атрибуте total_calls.
"""


def count_calls():
    counter = 0

    def inner():
        nonlocal counter
        counter += 1
        inner.total_calls = counter
        return counter

    inner.total_calls = 0
    return inner


counter = count_calls()
counter()
counter()
print(counter.total_calls)
counter()
print(counter.total_calls)

counter1 = count_calls()
counter2 = count_calls()
counter1()
print(counter1.total_calls, counter2.total_calls)
counter1()
counter2()
print(counter1.total_calls, counter2.total_calls)
counter2()
counter2()
print(counter1.total_calls, counter2.total_calls)
