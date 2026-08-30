""" 
Вновь словарь
На предыдущем уроке вы решали задачу «Словарь».  
В ней гарантировалось, что в сопрограмму alphabet будут передаваться только значения,
которые являются ключами глобальной переменной DICTIONARY.

Теперь вам необходимо переписать сопрограмму alphabet  так, 
чтобы она могла обрабатывать исключение KeyError. В  случае, когда возникнет исключение KeyError, 
сопрограмма должна генерировать значение «default».

Переменная DICTIONARY вам в редакторе кода по-прежнему не видна, 
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
    key = yield
    while True:
        try:
            key = yield DICTIONARY.get(key, "default")
        except KeyError:
            key = yield "default"
        

coro = alphabet()
next(coro)
print(coro.send('a'))
print(coro.send('b'))
print(coro.throw(KeyError))
print(coro.send('c'))

coro = alphabet()
next(coro)
for letter in 'qwerty':
    print(coro.send(letter))
    print(coro.throw(KeyError))
