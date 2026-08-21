""" 
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
                  
Ваша задача — написать генератор-функцию alphabet, 
которая на каждом шаге возвращает кортеж из двух элементов:

(ключ, значение)
                  
Генератор-функция alphabet должна выдавать значения в том же порядке, 
в котором были созданы ключи в словаре DICTIONARY. 
То есть генератор должен работать аналогично перебору словаря через .items().

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
    for k, v in DICTIONARY.items():
        yield k, v


g = alphabet()
letter, word = next(g)
print(letter, word)
print(next(g))
print(next(g))

for letter, word in alphabet():
    print(letter, word)
