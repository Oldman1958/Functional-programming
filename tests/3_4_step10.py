"""
Ваша задача написать функцию add_item, которая добавляет в корзину (глобальная переменная shopping_list) товар
и его количество.

Функция add_item обязательно должна принимать имя товара и необязательно - его количество (по умолчанию оно равно 1)
"""

shopping_list = {}


def add_item(perch, qt=1):
    if perch not in shopping_list:
        shopping_list[perch] = qt
    else:
        shopping_list[perch] = shopping_list[perch] + qt





add_item("Bread", 10)
add_item("Potato", 5)
add_item("Milk")
add_item("Orange", 3)
add_item("Orange", 2)
add_item("Milk")
add_item("Bread", 3)

print(shopping_list)
