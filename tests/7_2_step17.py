"""
Числа Трибоначчи
Ваша задача - написать рекурсивную функцию tribonacci,
которая принимает на вход целое число n - порядковый номер чисел Трибоначчи.
Функция по параметру n должна вычислить и вернуть значение,
стоящее на n-м месте в ряде чисел Трибоначчи



Ваша задача только написать определение функции tribonacci
"""


def tribonacci(n):
    if n == 0: return 0
    if n == 1: return 0
    if n == 2: return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


print(tribonacci(1))
print(tribonacci(8))
print(tribonacci(9))
print(tribonacci(10))
