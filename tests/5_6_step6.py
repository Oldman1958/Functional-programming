"""
Перед вами код из предыдущего задания. Исправьте его так, чтобы на экране появилась строка «hello», затем «bye»
"""


def outer(param = 'h') -> None:
    def say_hello() -> None:
        print('hello')

    def say_bye() -> None:
        print('bye')

    if param == 'h':
        say_hello()
    elif param == 'b':
        say_bye()
    else:
        print('I do not what to say')

#say_hello()
#say_bye()
outer('h')
outer('b')