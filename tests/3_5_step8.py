"""
Помните функцию words_length, которая по входному списку слов создавала список длины соответствующих слов
и возвращала его в качестве результата?
Одна из возможных реализаций этой функции представлена ниже

def words_length(words):
    return [len(word) for word in words]

Здесь функция words_length является чистой.
Ваша задача переписать ее так, чтобы она начала изменять входной список: вместо слов должна подставляться его длина.
В качестве результата новая words_length должна вернуть None
"""
words = ['Hello', 'world!']


def words_length(w):
    global words
    words = [len(word) for word in w]
    return None


words_length(words)
print(words)

"""
words = ['Python', 'is', 'awesome!']
words = words_length(words)
print(words)
"""

