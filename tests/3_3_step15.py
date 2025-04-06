"""
Через некоторое время менеджеры ресторана поняли, что помимо имени клиента, они бы еще хотели хранить его принадлежность
к статусу VIP клиента. Соответственно, они бы хотели изменить структуру хранения резерваций на следующую:

tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False},
    6: None,
    7: None,
    8: None,
    9: None,
}
Здесь мы видим, что информация о клиенте хранится во вложенном словаре, у которого имеется два ключа name и is_vip.

Исходя из новой структуры данных, ваша задача теперь сделать рефакторинг кода функции reserve_table.
Теперь она должна принимать не два аргумента, а три: номер стола, имя клиента и статус VIP.
Делать проверку свободен и если она пройдена, сохранять данные в описанной выше структуре

Для успешного прохождения тестов скопируйте также реализацию функции delete_reservation  из задания «Резервация столов»
и все ее зависимости от других функций, если они были
"""
tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False},
    6: None,
    7: None,
    8: None,
    9: None,
}


def is_table_free(table):
    if tables[table] is None:
        return True
    else:
        return False


def reserve_table(table, nam, is_vip):
    if is_table_free(table):
        tables[table] = {'name':nam, 'is_vip':is_vip}



def delete_reservation(table):
    tables[table] = None


reserve_table(6, 'Ann', True)


print(tables)

delete_reservation(6)

print(tables)
