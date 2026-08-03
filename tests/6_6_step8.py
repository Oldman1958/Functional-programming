"""
Перед вами кортеж english_words

При помощи enumerate обойдите слова этой коллекции и для каждого элемента выведите строку вида

Word № {number} = {word}

Например, для кортежа english_words = ('hi', 'World') ответ был бы таким:

Word № 1 = hi
Word № 2 = World

Обратите внимание, что нумерация слов начинается с единицы
"""

english_words = ('attack', 'bless', 'look', 'reckless', 'short', 'monster', 'trolley', 'sound',
                 'ambiguity', 'researcher', 'trunk', 'coat', 'quantity', 'question', 'tenant',
                 'miner', 'definite', 'kit', 'spectrum', 'satisfied', 'selection', 'carve',
                 'ask', 'go', 'suggest')

for number, word in enumerate(english_words, start=1):
    print(f"Word № {number} = {word}")
