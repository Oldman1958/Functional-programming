"""
Двойной факториал
Необходимо написать рекурсивную функцию double_fact,
которая принимает на вход целое число и вычисляет значение двойного факториала по формуле:
        1                           if n = 1
F(n) =  2                           if n = 2
        n*(n-2)*(n-4)*(n-6)...      if n > 2

Ваша задача только написать определение функции double_fact
"""


def double_fact(n):
    if n == 1: return 1
    if n == 2: return 2
    return double_fact(n - 2) * n


print(double_fact(6))
print(double_fact(5))