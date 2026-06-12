"""
Удаляем заказ
Вам потребуется код из задачи «Делаем заказ в ресторане»

От менеджеров поступило требование написать функционал, который позволяет очищать заказ.
Для этого нужно разработать функцию delete_order, которая имеет следующие параметры

обязательный ключевой параметр number_table - номер стола, где будем очищать заказ

необязательный ключевой параметр delete_all со значением по умолчанию False.
Если передать в него True, должна очищаться полностью информация о заказе для указанного столика.
При значении False удаление в заказе будет точечным по категориям

произвольное количество ключевых параметров с булевым значением вида
drink=True, desert=True, call=True, шаурма=True


Среди этих значений вам нужно удалять из заказа только те, имена которых находятся в списке категорий
и переданное значение равно True

Для успешного решения задания вам необходимо определить новую функцию delete_order
 и продублировать ранее созданные reserve_table и make_order со всеми их зависимостями.
"""

# Глобальная переменная с данными о столах
tables = {
    1: None, 2: None, 3: None, 4: None,
    5: None, 6: None, 7: None, 8: None, 9: None
}

# Список допустимых категорий меню
MENU_CATEGORIES = {'salad', 'soup', 'main_dish', 'drink', 'desert'}

def is_table_free(num_table):
    """Проверяет, свободен ли стол с указанным номером."""
    return tables.get(num_table) is None

def reserve_table(num_table, name, vip=False):
    """
    Резервирует стол для посетителя.

    Args:
        num_table (int): номер стола;
        name (str): имя посетителя;
        vip (bool): флаг VIP‑статуса (по умолчанию False).
    """
    if is_table_free(num_table):
        tables[num_table] = {
            'name': name,
            'is_vip': vip,
            'order': {}  # Поле для хранения заказа — пустой словарь
        }
    return tables

def make_order(num_table, **kwargs):
    """
    Добавляет заказ для указанного стола.

    Args:
        num_table (int): номер стола;
        **kwargs: пары категория=блюдо для заказа.
    """
    # Проверяем, существует ли стол и зарезервирован ли он
    if num_table not in tables or tables[num_table] is None:
        return

    # Получаем текущий заказ стола
    current_order = tables[num_table]['order']

    # Обрабатываем каждую пару категория=блюдо из kwargs
    for category, dish in kwargs.items():
        # Добавляем в заказ только если категория есть в меню
        if category in MENU_CATEGORIES:
            current_order[category] = dish

def delete_order(*, number_table, delete_all=False, **kwargs):
    """
    Удаляет заказ или его части для указанного стола.

    Args:
        number_table (int): номер стола, где будем очищать заказ;
        delete_all (bool): если True — очищается вся информация о заказе,
                          если False — удаление точечное по категориям (по умолчанию False);
        **kwargs: произвольное количество ключевых параметров с булевым значением,
                  где имя параметра — категория блюда, значение — флаг удаления (True/False).
    """
    # Проверяем, существует ли стол и зарезервирован ли он
    if number_table not in tables or tables[number_table] is None:
        return

    # Получаем текущий заказ стола
    current_order = tables[number_table]['order']

    if delete_all:
        # Полностью очищаем заказ — заменяем на пустой словарь
        current_order.clear()
    else:
        # Точечное удаление: удаляем только те категории, которые есть в MENU_CATEGORIES
        # и для которых передано значение True
        categories_to_delete = [
            category for category, should_delete in kwargs.items()
            if should_delete and category in MENU_CATEGORIES
        ]
        for category in categories_to_delete:
            current_order.pop(category, None)  # pop с None — безопасный вариант: не вызовет ошибку, если ключа нет




