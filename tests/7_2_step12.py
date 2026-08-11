"""
Сумма цифр числа
Напишите функцию sum_digits, которая находит сумму всех цифр переданного натурального числа n

Ваша задача только написать определение функции sum_digits
"""


def sum_digits(num):
    nums = str(num)
    if len(nums) == 1:
        return int(nums[0])
    return int(nums[0]) + sum_digits(nums[1:])


print(sum_digits(345))
print(sum_digits(45))
print(sum_digits(5))
