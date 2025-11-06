"""
Перепишите функцию rotate так, чтобы она стала работать не со списками, а с кортежами.
Для этого выполните следующие шаги:

    1️ переименовать параметр lst - в tpl. Теперь функция будет принимать не список,
    а кортеж целых или вещественных чисел

    2️ изменится тип возвращаемого значения. Вместо списка функция rotate теперь должна возвращать кортеж.
    Остальная логика программы не меняется

    3️ док строку изменить на «Функция выполняет циклический сдвиг кортежа на shift позиций вправо (shift>0)
    или влево (shift<0)»
"""


def rotate(tpl: tuple[int | float, ...], shift: int = 1) -> tuple[int | float, ...]:
    """Функция выполняет циклический сдвиг кортежа на shift позиций вправо (shift>0) или влево (shift<0)"""
    new_tpl = list(tpl)
    if shift < 0:
        steps = abs(shift)
        for i in range(steps):
            new_tpl.append(new_tpl.pop(0))
    elif shift > 0:
        for i in range(shift):
            new_tpl.insert(0, new_tpl.pop())

    return tuple(new_tpl)


print(rotate.__doc__)
print(rotate.__annotations__)
print(rotate((1, 2, 3, 4, 5, 6, 7), 2))
