"""
Одной из базовых банковских услуг является обмен валют.

Напишите функцию convert, которая умеет конвертировать доллар в другую валюту и наоборот.
Для конвертации используются текущие курсы валют, которые хранятся в глобальном словаре exchange_rates.

Результат округлите до двух знаков после запятой при помощи функции round
"""
from typing import Optional

exchange_rates = {
    "USD": 1.0,
    "EUR": 0.861775,
    "GBP": 0.726763,
    "INR": 75.054725,
    "AUD": 1.333679,
    "CAD": 1.237816,
    "SGD": 1.346851,
}


def convert(inn: str, out: str, m: int) -> Optional[float]:
    """Функция конвертирует курс валют"""
    result = round((exchange_rates[out] * m) / exchange_rates[inn], 2)
    return result


currency = convert("USD", "EUR", 100)
print(currency)
