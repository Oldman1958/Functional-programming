"""
Функция aggregation - 3
Перепишите функцию aggregation с прошлого шага так,
чтобы у нее появился необязательный параметр initial по умолчанию равный None.
Данный параметр отвечает за начальное состояние агрегации, если в него передать значение.
Если ничего не передавать в initial, то функция aggregation работает как прежде.
"""

def aggregation(func, sequence, initial=None):
    # Если последовательность пустая
    if not sequence:
        # Если задано начальное значение, возвращаем его
        if initial is not None:
            return initial
        # Иначе возвращаем None (нет значения для агрегации)
        else:
            return None

    # Если задано начальное состояние агрегации
    if initial is not None:
        current_value = initial
        # Проходим по всем элементам последовательности
        for element in sequence:
            current_value = func(current_value, element)
    else:
        # Если в последовательности только один элемент, возвращаем его
        if len(sequence) == 1:
            return sequence[0]

        # Начальное значение — первый элемент последовательности
        current_value = sequence[0]
        # Проходим по оставшимся элементам последовательности (начиная со второго)
        for element in sequence[1:]:
            # Применяем функцию func к текущему накопленному значению и следующему элементу
            current_value = func(current_value, element)

    # Возвращаем итоговое агрегированное значение
    return current_value
