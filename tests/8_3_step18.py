""" 
Словарь
В вашем распоряжении имеется глобальная переменная DICTIONARY, представляющая собой словарь, 
где ключами являются английские буквы, а значениями - слова, начинающиеся с буквы ключа. 
Начальное заполнение DICTIONARY имеет следующий вид:

DICTIONARY = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cat',
    'd': 'dog',
    ...
}

                  
Ваша задача — написать сопрограмму alphabet, в которую передаются буквы, 
а в ответ она генерирует слова, закрепленные переданной буквой из словаря DICTIONARY.

Гарантируется, что в alphabet будут поступать значения, 
которые имеются в ключах словаря DICTIONARY.

Сама переменная DICTIONARY вам в редакторе кода не видна, 
но вы можете обращаться к ней внутри сопрограммы alphabet.
"""

DICTIONARY = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cat',
    'd': 'dog',
    'e': 'elephant',
    'f': 'fox',
    'g': 'gorilla',
    'h': 'hippo',
    'i': 'iguana',
    'j': 'jaguar',
    'k': 'koala',
    'l': 'llama',
    'm': 'monkey',
    'n': 'newt',
    'o': 'octopus',
    'p': 'parrot',
    'q': 'quail',
    'r': 'rabbit',
    's': 'squirrel',
    't': 'tiger',
    'u': 'unicorn',
    'v': 'viper',
    'w': 'walrus',
    'x': 'xenomorph',
    'y': 'yak',
    'z': 'zebra'
}


def alphabet():
    letter = yield  # первый yield нужен, чтобы запустить корутину через next()
    while True:
        letter = yield DICTIONARY[letter]



coro = alphabet()
next(coro)
print(coro.send('a'))
print(coro.send('b'))
print(coro.send('c'))
