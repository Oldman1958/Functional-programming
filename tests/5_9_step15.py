"""
Чиним баги Кузьмы
Программист Кузьма познакомился с декораторами и решил написать свой первый пример,
где он пытался сопроводить вызов функции add дополнительными выводами на экран.
Вот что получилось:

def decorator(func):
    def wrapper():
        print('---Start calculation---')
        result = func()
        print(f'---Finish calculation. Result is {result}---')
        return result
    return wrapper


@decorator
def add(a, b):
    return a + b


По его задумке декоратор должен сопровождать вызов декорируемой функции сообщениями

---Start calculation---

и

---Finish calculation. Result is {result}---

Но во время тестирования функции add Кузьма столкнулся с ошибкой
takes 0 positional arguments but 2 were given

Помогите исправить его декоратор так, чтобы все заработало.

Для проверки правильности работы программы перед непосредственной отправкой
пользуйтесь кнопкой «Запустить».
"""


def decorator(func):
    def wrapper(*args):  # Добавили произвольное количество позиционных аргументов
        print('---Start calculation---')
        result = func(*args)  # Добавили произвольное количество позиционных аргументов
        print(f'---Finish calculation. Result is {result}---')
        return result

    return wrapper


@decorator
def add(a, b):
    return a + b
