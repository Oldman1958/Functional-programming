"""
Перепишите функцию print_results так, чтобы информация выводилась по убыванию оценок,
а в случае их равенства предметы должны выводиться в обратном алфавитном порядке без учета регистра
"""


def print_results(tpl):
    res = sorted(tpl, key=lambda x: (int(x[1]), x[0].lower()), reverse=True)
    for elem in res:
        print(*elem)


marks = [('English', 88), ('Science', 90), ('Maths', 88),
         ('Physics', 93), ('History', 78), ('French', 78),
         ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
print_results(marks)
