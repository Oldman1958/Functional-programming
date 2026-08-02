"""
Лучшая оценка - 2
 Усовершенствуйте функцию get_info_marks из предыдущего урока так, чтобы она возвращала словарь,
 в котором для каждого студента формируется словарь,
 хранящий информацию как о лучшей оценке студента(ключ «best»), так и худшей (ключ «worst»)

Параметры функции остаются неизменными.
"""


def get_info_marks(stds, *marks):
    """
    Возвращает словарь: ключ—имя студента, значение—словарь с лучшей ('best')
    и худшей ('worst') оценкой студента.

    :param stds: список имён студентов (обязательный параметр)
    :param marks: произвольное количество списков с оценками (по одному списку на экзамен)
    :return: словарь вида {имя_студента: {'best': макс_оценка, 'worst': мин_оценка}}
    """
    # zip объединяет оценки по позициям: для каждого студента получаем кортеж его оценок
    students_marks = zip(*marks)

    # Для каждого студента находим max и min оценки и формируем пару (имя, {best, worst})
    result_pairs = map(lambda pair: (pair[0], {"best": max(pair[1]), "worst": min(pair[1])}), zip(stds, students_marks))

    return dict(result_pairs)


math = [90, 76, 94]
history = [78, 79, 90]
students = ["Marie", "Michael", "Marge"]
print(get_info_marks(students, math, history))

math = [90, 76, 94]
history = [78, 79, 90]
geography = [95, 80, 92]
students = ["Marie", "Michael", "Marge"]
print(get_info_marks(students, math, geography, history))
