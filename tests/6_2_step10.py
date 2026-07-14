"""
Программе на вход поступают слова, разделенные пробелом.
Ваша задача - проверить, во всех ли словах есть английская буква A вне зависимости от регистра.
В качестве ответа программа должна вывести True или False.
"""

print(all(["A" in word.upper() for word in input().split()]))

# chase enlarge referee cup offense - False
# acquaintance disAgree- True