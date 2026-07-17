"""
Напишите функцию get_letters, которая принимает строку и формирует из нее список кортежей.
Каждый элемент кортежа будет состоять из двух значений:
берется соответствующая буква сперва в верхнем регистре, а затем в нижнем (см. примеры ниже)
"""


def get_letters(string):
    return [(letter.upper(), letter.lower()) for letter in string]


print(get_letters('TykPe'))

print(get_letters('MeSsi'))

print(get_letters('WelLDone'))