"""
Мы часто сталкиваемся с математической проблемой, когда после совместного похода в ресторан необходимо посчитать
сколько должен каждый человек. Давайте создадим функцию calculate_per_person, которая поможет выполнить расчет.

Будем считать, что у нас идеальная ситуация, когда между N количеством людей нужно разделить счет поровну.
Также в счет нужно включить чаевые официанту, которые по умолчанию составляют 10%.

Итого получаем, что функция calculate_per_person может принимать следующие аргументы

обязательно счет за ресторан
обязательно количество людей
необязательно процент чаевых официанту, по умолчанию 10%

Функция calculate_per_person должна вернуть результат - сумму, которую должен заплатить каждый участник ужина.

При расчете у вас будут возникать вещественные числа, результат нужно будет округлять функцией round до второго
разряда после запятой.
"""

def calculate_per_person(bill, n, tea=10):
    return round((bill * ((100 + tea) / 100)) / n, 2)


print(calculate_per_person(200.0, 4, 50))
