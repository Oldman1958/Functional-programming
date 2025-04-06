"""
Панграмма — это предложение, которое содержит все буквы алфавита хотя бы один раз.
В нашем задании мы будем рассматривать в качестве алфавита буквы английского языка.
Тогда одним из примеров панграммы будет фраза «The quick brown fox jumps over the lazy dog».

Ваша задача здесь — написать функцию is_pangram для проверки предложения на предмет того,
является ли оно панграммой или нет. Для проверок внутри функции вы можете пользоваться глобальной переменной alpha.
Символы, которые не являются буквами, необходимо игнорировать.
"""


def is_pangram(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in alpha:
        if i in s or i.upper() in s:
            continue
        else:
            return False
    return True

# print(is_pangram("How quickly daft jumping zebras vex!"))
