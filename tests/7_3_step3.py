"""
Проверка на вхождение через рекурсию
Перепишите реализацию функции is_member через рекурсию.
Напоминаю, функция is_member  должна проверять, есть ли значение value в линейном списке lst.

Функция is_member должна вернуть True, если значение value присутствует в списке lst,
и False в противном случае.

Гарантируется, что список lst не будет вложенным
"""


def is_member(value, lst):
    if not lst:
        return False
    if lst[0] == value:
        return True
    return is_member(value, lst[1:])


print(is_member("e", ['a', 'e', 'i', 'o', 'u']))
print(is_member(10, [1, 23, 3, 43, 10, 35]))
print(is_member('might', ['or', 'maybe', 'this']))
