"""
Напишите функцию truncate_sentences, которая обрезает предложения и оставляет из них только первые N символов.
Количество предложений, которые поступают на вход функции, может быть произвольным
"""


def truncate_sentences(n, *args):
    res = []
    for i in args:
        res.append(i[:n])

    print(*res, sep='\n')
