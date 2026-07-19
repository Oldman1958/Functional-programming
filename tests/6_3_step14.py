"""
Обратное преобразование
В базовом курсе по python есть задача RGB ,
в которой необходимо по трем целым числам получить цвет в формате RGB.
Сейчас вам предстоит выполнить обратное преобразование

Ваша задача создать функцию from_hex_to_rgb,
которая принимает на вход строку - закодированный код цвета в формате RGB
и возвращает кортеж из трех значений (оттенок_красного, оттенок_зеленого, оттенок_синего).
Вот посмотрите примеры:

from_hex_to_rgb(#000000) => (0, 0, 0)
from_hex_to_rgb(#FFFFFF) => (255, 255, 255)
from_hex_to_rgb(#FF0000) => (255,0, 0)
from_hex_to_rgb(#00FF00) => (0,255, 0)
from_hex_to_rgb(#0000FF) => (0,0,255)
from_hex_to_rgb(#FFFFFF) => (255,255,255)
from_hex_to_rgb(#87CEEB) => (135,206,235)
from_hex_to_rgb(#87CEFA) => (135,206,250)
from_hex_to_rgb(#191970) => (25,25,112)

Как только функция будет готова, ее необходимо использовать внутри функции convert_to_rgb,
которая принимает список строк, содержащих информацию о цветах в формате RGB.
Функция convert_to_rgb должна расшифровать каждый цвет и вернуть список кортежей.
"""


def from_hex_to_rgb(color: str) -> tuple[int, int, int]:
    # Убираем символ '#', если он есть
    hex_str = color.lstrip('#')

    # Разбиваем строку на пары символов для R, G, B
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)

    return r, g, b


def convert_to_rgb(values: list[str]) -> list[tuple[int, int, int]]:
    return list(map(from_hex_to_rgb, values))


# Пример использования:
print(from_hex_to_rgb('#B22222'))
print(from_hex_to_rgb('#FFFFFF'))
print(from_hex_to_rgb('#000000'))
print(from_hex_to_rgb('#87CEEB'))
print(from_hex_to_rgb('#191970'))
