"""
Перед вами имеется реализация функции get_values

Ваша задача — избавиться от циклов for при помощи map и filter.
Для этого перепишите функцию get_values, но так,
чтобы она не меняла свою изначальную функциональность

def get_values(nums: tuple[int, ...]) -> tuple[int, ...]:
    lst = []
    for i in nums:
        if i % 3 == 0:
            lst.append(i)

    for i in range(len(lst)):
        lst[i] = lst[i] * 3

    return tuple(lst)

"""


def get_three(x):
    return x * 3


def get_values(nums: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(map(get_three, filter(lambda x: x % 3 == 0, nums)))


nums = (2, 12, 5, 9, 3, 16, 7, 13, 21, 1, 15, 4, 20, 11)
print(get_values(nums))

nums = (2, 0, 3, 4, 7, 13, 21, 1, 15, 9, 11)
print(get_values(nums))
