"""
Декоратор uppercase_elements
Ваша задача написать логику работы декоратора uppercase_elements,
который умеет работать с функциями, возвращающими коллекции элементов.
Задача декоратора uppercase_elements преобразовать каждый строковый элемент коллекции
к заглавному регистру.
В случае, если оригинальная функция возвращает словарь,
то элементом считаем только строковые ключи словаря.

Элементы, не являющиеся строкой, не должны изменяться декоратором uppercase_elements

Гарантируется, что коллекции, возвращаемые оригинальной функцией, не являются вложенными
"""

def uppercase_elements(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if isinstance(result, dict):
            # Обрабатываем только строковые ключи, значения оставляем без изменений
            new_dict = {}
            for key, value in result.items():
                if isinstance(key, str):
                    new_dict[key.upper()] = value
                else:
                    new_dict[key] = value
            return new_dict

        elif isinstance(result, (list, tuple, set)):
            # Для последовательностей и множеств обрабатываем каждый элемент
            if isinstance(result, list):
                return [item.upper() if isinstance(item, str) else item for item in result]
            elif isinstance(result, tuple):
                return tuple(item.upper() if isinstance(item, str) else item for item in result)
            elif isinstance(result, set):
                return {item.upper() if isinstance(item, str) else item for item in result}

        # Если тип не поддерживается, возвращаем результат без изменений
        return result

    return wrapper

@uppercase_elements
def my_func():
    return ['monarch', 'Touch', 'officiaL', 'DangerouS', 'breathe']

print(my_func())

@uppercase_elements
def my_func(name, surname):
    return ['temple', 'store', name, surname, *[1, 2, 3]]

print(my_func('Gerard', 'Pique'))

