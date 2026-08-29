"""
Нахождение среднего арифметического
Ваша задача — создать корутину get_average, 
которая накапливает среднее арифметическое переданных в нее чисел.

Числа поступают в корутину при помощи метода send, 
корутина должна порождать текущее накопленное значение среднего арифметического. 

Вам необходимо написать только определение функции-корутины get_average.
"""


"""def get_average():
    res = []
    average = 0
    while True:
        value = yield average
        res.append(value)
        average = sum(res) / len(res)"""


def get_average():
    total = 0
    count = 0

    # Первый yield — просто чтобы «разбудить» корутину через next()
    value = yield

    while True:
        total += value
        count += 1
        # Сразу возвращаем среднее — его и получит send()
        value = yield total / count



coro = get_average()
next(coro)
print(coro.send(10))
print(coro.send(20))
print(coro.send(6))
