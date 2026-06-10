"""
Хорошо постарались с прошлой задачей!
Однако мы забыли, что скидка должна быть только для тех товаров, стоимость которых больше 50.
Вам стоит внести это изменение в прошлый код

Ваша задача только переопределить переменную sale_lambda
"""

sale_lambda = lambda x: x * 0.9 if x > 50 else x

print(sale_lambda.__name__)
print(sale_lambda(50.0))
print(sale_lambda(60.0))
print(sale_lambda.__name__)