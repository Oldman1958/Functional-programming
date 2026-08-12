"""
Функция Аккермана
Ваша задача - написать рекурсивную функцию ackermann,
которая принимает на вход два целых числа m и n, и находит значение, определенное следующим образом:



Найденное значение функция ackermann должна вернуть в качестве результата

Ваша задача только написать определение функции ackermann

В тестовых примерах в функцию сперва передается значение параметра m, затем n.
"""


def ackermann(m, n):
    if m == 0: return n + 1
    if m > 0 and n == 0: return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(1, 5))
print(ackermann(2, 4))
print(ackermann(3, 3))
print(ackermann(3, 2))

