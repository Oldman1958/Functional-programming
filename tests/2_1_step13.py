"""
В вашем распоряжении имеется две функции: say_hello и choose_profession

Ваша задача вызвать сперва say_hello и передать значение Артем, а затем вызвать choose_profession со значением Разработчик

Sample Input:

Sample Output:

Привет, Артем!
Я хочу стать Разработчиком
"""


def say_hello(name):
    print(f"Привет, {name}!")


def choose_profession(profession):
    print(f'Я хочу стать {profession}ом')


say_hello('Артем')
choose_profession('Разработчик')

