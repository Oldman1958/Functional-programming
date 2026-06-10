"""
В переменную check_word присвойте lambda функцию, которая принимает строку и возвращает True,
если переданная строка начинается с букв «Q» или «R» и заканчивается любой из гласных «A», «E», «I», «U» или «O».
Регистр во время проверок не должен иметь значения

Во всех остальных случаях нужно возвращать False

Ничего кроме создания переменной check_word делать не нужно
"""

check_word = lambda s: True if s[0] in 'QRqr' and s[-1] in 'AEIUOaeiuo' else False

print(check_word.__name__)
print(check_word('radio'))

print(check_word('raid'))
print(check_word.__name__)

print(check_word('revenge'))