""" 
Функция-генератор chunker
Если у вас есть итерируемый объект, который слишком велик для того, 
чтобы полностью поместиться в памяти (например, при работе с большими файлами), 
возможность дробить его на небольшие фрагменты 
и затем использовать их за раз может быть очень ценной.

С этой задачей должна справиться функция-генератор chunker. 
Она должна принимать итерируемый объект и выдавать фрагмент указанного размера за раз.

Ваша задача написать функцию-генератор chunker
"""


def chunker(obj, stp):
    start, end = 0, stp
    for i in range(start, len(obj), stp):
        try:
            yield obj[start: end]
            start, end = end, end + stp
           
        except:

            yield obj[start:]


for chunk in chunker(range(25), 4):
    print(list(chunk))
for chunk in chunker(range(56), 9):
    print(list(chunk))
