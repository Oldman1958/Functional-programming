"""
Функция replace должна возвращать новую строку, в которой все символы old были заменены на new.
При замене регистр букв должен учитываться

replace('Нет', 'т') => 'Не'
replace('Bella Ciao', 'a') => 'Bell Cio'
replace('nobody; i myself farewell analysis', 'l', 'z') => 'nobody; i mysezf farewezz anazysis'
replace('commend me to my kind lord meaning', 'M', 'w') => 'commend me to my kind lord meaning'
Ваша задача дописать только тело функции replace
"""


def replace(text, old, new=''):
    return text.replace(old, new)

print(replace('Нет', 'т'))
print(replace('Bella Ciao', 'a'))
print(replace('nobody; i myself farewell analysis', 'l', 'z'))
