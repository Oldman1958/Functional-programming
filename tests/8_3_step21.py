""" 
Проверка пароля
Ваша задача — создать сопрограмму check_password, 
которая проверяет поступающий ей пароль на безопасность.

С точки зрения безопасности будет подходить пароль, 
для которого одновременно выполняются следующие условия:

длина не менее 10 символов;
должна присутствовать хотя бы одна заглавная буква латинского алфавита;
должна присутствовать хотя бы одна цифра;
должен присутствовать хотя бы один служебный символ из набора !, @, #, $, %.
Пароли в виде строки поступают в сопрограмму при помощи метода send. 
Сопрограмма должна порождать значение True, если пароль соответствует всем перечисленным условиям, 
в противном случае - значение False. 

Вам необходимо написать только определение функции-сопрограммы check_password.
"""


def check_password():
    special_chars = set("!@#$%")
    pwd = yield  # первый yield — чтобы дойти сюда через next(coro)

    while True:
        has_upper = any(c.isupper() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_special = any(c in special_chars for c in pwd)

        result = (
            len(pwd) >= 10 and
            has_upper and
            has_digit and
            has_special
        )

        pwd = yield result  # сразу возвращаем результат, принимаем следующий пароль


passwords = [
    'QwerTY123@', 'QwerTY!@#$', 'QwerTY!@#4',
    'qwerty!@#4', 'qweRty!@#4'
]
coro = check_password()
next(coro)
for pas in passwords:
    print(coro.send(pas))
