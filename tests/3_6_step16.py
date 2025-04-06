"""
Давайте теперь создадим функцию print_goods, которая печатает список покупок.
На вход она будет принимать произвольное количество значений, а товаром мы будем считать любые непустые строки.
Следовательно, все числа, списки, словари и другие нестроковые объекты вам нужно будет проигнорировать.

Функция print_goods должна печатать список товаров в виде: «<Порядковый номер товара>. <Название товара>».
На примерах ниже вы можете посмотреть как должна работать функция print_goods

print_goods('apple', 'banana', 'orange')
# Программа должна вывести следующее:
1. apple
2. banana
3. orange
"""


def print_goods(*args):
    out = []
    for i in args:
        if isinstance(i, str) and len(i) > 0:
            out.append(i)
    if len(out) == 0:
        print('Нет товаров')
    else:
        for i in range(len(out)):
            if len(out) > 0:
                print(f'{i}. {out[i]}')




# print_goods('apple', 'banana', 'orange')
print_goods(1, True, 'Грушечка', '', 'Pineapple')
print_goods([], {}, 1, 2)
