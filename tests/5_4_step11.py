"""
Перепишите функцию print_results так, чтобы информация выводилась по убыванию оценок.

В случае равенства оценок предметы должны выводиться на экран в том же порядке,
в котором они следовали во входном списке
"""


def print_results(tpl):
    res = sorted(tpl, key=lambda x: x[1], reverse=True)
    for elem in res:
        print(*elem)


marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]
print_results(marks)

marks = [('English', 88), ('Science', 100), ('Maths', 81),
         ('Physics', 100), ('History', 82), ('Music', 100)]
print_results(marks)
