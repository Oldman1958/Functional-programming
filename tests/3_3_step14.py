"""
Продолжаем автоматизировать работу ресторана.
Следующий этапом является резервация(закрепление) свободного столика за клиентом и отмена брони.
Структура хранения резерваций все та же в виде словаря:

tables = {
  1: 'Andrey',
  2: None,
  3: None,
  4: None,
  5: None,
  6: None,
  7: None,
  8: None,
  9: None,
}
Ваша задача написать две функции, которые помогут создавать и удалять бронирование:

✔  функцию reserve_table, которая принимает номер стола и имя клиента,
проверяет свободен ли указанный столик и если за ним никто не прикреплен, вносятся данные клиента.
Больше данная функция ничего не делает.
Для реализации этой функции можете воспользоваться функцией is_table_free из задания «Автоматизируем ресторан:
вакантные столы»

✔ функцию delete_reservation, которая очищает запись о бронировании.
"""
tables = {
    1: 'Andrey',
    2: None,
    3: None,
    4: None,
    5: None,
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


def reserve_table(table, name):
    if is_table_free(table):
        tables[table] = name


def delete_reservation(table):
    tables[table] = None


reserve_table(5, 'Ann')

print(tables)

delete_reservation(5)

print(tables)
