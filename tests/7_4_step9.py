""" 
Превращаем вложенный словарь в плоский
Перед вами имеется вложенный словарь, уровень вложенности произвольный и заранее неизвестен. 
Ключами словаря на любом уровне могут быть только строки, значениями - только числа. 

Учитывая указанные выше условия, ваша задача состоит в том, 
чтобы преобразовать этот вложенный словарь в плоский (состоящий только из одного уровня), 
где ключи формируются конкатенацией вложенных ключей, соединенных знаком _

Для этого необходимо определить рекурсивную функцию flatten_dict. 
Она должна принимать вложенный словарь и возвращать плоский.

Ваша задача только написать определение функции flatten_dict.
"""


def flatten_dict(dct, parent_key='', sep='_'):
    result_dct = {}
    for k, v in dct.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            result_dct.update(flatten_dict(v, new_key, sep=sep))
        else:
            result_dct[new_key] = v
    return result_dct


print(flatten_dict({'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}))
print(flatten_dict({'Germany_berlin': 7,
                    'Europe_italy_Rome': 3,
                    'USA_washington': 1,
                    'USA_New York': 4}))
