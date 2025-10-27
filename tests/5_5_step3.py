"""
Напишите функцию get_info_about_object, которая принимает объект и выводит информацию обо всех его атрибутах
и методах в следующем формате:

сперва выводится список всех атрибутов и методов
на следующей строке фраза «Всего у объекта {count} атрибутов и методов»

Примечание: тестирование на платформе будет производиться на версии Python 3.12, поэтому не переживайте,
если вы используете у себя на устройстве другую версию python и у вас не совпадает вывод.
"""


def get_info_about_object(target):
    print(dir(target))
    print(f"Всего у объекта {len(dir(target))} атрибутов и методов")


def print_goods(lst):
    pass


get_info_about_object(print_goods)


def print_goods(lst):
    pass


print_goods.info = 'Функция для вывода информации о товарах'
print_goods.is_working = False
print_goods.status = 'Not ready'

get_info_about_object(print_goods)

get_info_about_object(str)
