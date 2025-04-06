"""
Перепишите функцию my_func так, чтобы она стала чистой

def my_func(collection, n):
    for i in range(1, n + 1):
        collection.append(i)
    return collection
"""


def my_func(collection, n):
    coll_copy = collection[:]
    for i in range(1, n + 1):
        coll_copy.append(i)
    return coll_copy

a = [10, 20, 30]
res = my_func(a, 3)
print(a)
print(res)
