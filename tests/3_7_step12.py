"""
Студент-программист поспешил и неправильно написал программу. Теперь он имеет дело с ошибкой

TypeError: print_args() missing 3 required positional arguments: 'b', 'c', and 'd'

Помогите ему исправить вызов функции так, чтобы print_args смогла отработать и вывести числа на экран


def print_args(a, b, c, d):
    print(a, b, c, d)

dct = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
print_args(dct)
"""
def print_args(a, b, c, d):
    print(a, b, c, d)

dct = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
print_args(**dct)
