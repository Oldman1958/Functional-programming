"""
Делаем заказ в ресторане

ВНИМАНИЕ!!! ЗАДАЧА НЕ РЕШЕНА!!!

"""
menu = ["salad", "soup", "main_dish", "drink", "desert"]


def reserve_table(table, nam, is_vip=False, order={}):
    tables[table] = {
        'name': nam,
        'is_vip': is_vip,
        'order': order if order else {}
    }


def make_order(num, **kwargs):
    reserve_table(num)
    for k, v in kwargs.items():
        if k in menu:
            tables[table][order][k] = v


tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}

make_order(1, soup='Borsh')
make_order(1, desert='Наполеон', drink='Чай')
print(tables)