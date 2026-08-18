""" 
Поиск уровня
Создайте рекурсивную функцию find_level_element,
которая определяет на каком уровне вложенности располагается интересующий нас элемент. 
Нумерация уровней вложенности начинается с единицы.

Функция find_level_element принимает некое значение value и список значений lst.

Функция find_level_element должна вернуть номер уровня,
где встречается первое найденное значение value в списке lst на любом уровне. 
Если же в lst отсутствует значение value, функция find_level_element должна вернуть -1.
"""


def find_level_element(value, lst, level=1):
    for item in lst:
        if isinstance(item, list):
            # Рекурсивный поиск во вложенном списке на следующем уровне
            result = find_level_element(value, item, level + 1)
            if result != -1: return result
        elif item == value: return level
    return -1


print(find_level_element(5, [1, 2, 3, 4, 5, [5]]))
print(find_level_element(5, [1, 2, 3, 4, [[5]], [5]]))
print(find_level_element(9, [1, 2, 3, 4, [[5]], [5]]))
