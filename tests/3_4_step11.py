"""
Напишите функцию show_list, которая выводит список товаров из корзины (глобальная переменная shopping_list).
У функции show_list есть необязательный логический параметр include_quantities, по умолчанию принимает значение True.

Если include_quantities имеет значение True, вы должны выводить имя товара и его количество в следующем формате:

{количество}x{имя_товара},

иначе необходимо вывести только имя.

Напишите только реализацию функции show_list
"""

shopping_list = {'Bread': 13, 'Potato': 5, 'Milk': 2, 'Orange': 5}

def show_list(include_quantities=True):
    if include_quantities:
        for i in shopping_list:
            print(f'{shopping_list[i]}x{i}', end='\n')
    else:
        for i in shopping_list:
            print(f'{i}', end='\n')
show_list()