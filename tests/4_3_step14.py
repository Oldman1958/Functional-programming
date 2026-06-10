"""
Напишите функцию rotate_letter, которая принимает два аргумента:

letter - одна английская буква в нижнем регистре
shift целое число - значение сдвига буквы (может быть как положительным, так и отрицательным)
Функция rotate_letter по переданному значению сдвига shift находит новую букву
относительно текущей позиции буквы letter в алфавите.
Сдвиг может быть цикличным в пределах от a до z как в вправо (при положительном значении shift),
так и влево (при отрицательном значении shift). Ниже представлены примеры работы функции rotate_letter:

rotate_letter('b', 2)=> 'd'
rotate_letter('d', 1) => 'e'
rotate_letter('z', 1) => 'a'
rotate_letter('d', -2) => 'b'
rotate_letter('d', 26) => 'd'
rotate_letter('b', -3) => 'y'


Требования к функции rotate_letter:

     ✔️ должна вернуть новый символ;

     ✔️ параметры и возвращаемое значение должны быть проаннотированы;

     ✔️ добавьте doc-строку «Функция сдвигает символ letter на shift позиций».
"""


def rotate_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    letter = letter.lower()
    alfavit = 'abcdefghijklmnopqrstuvwxyz'

    if shift > 0:
        new_letter = alfavit[(alfavit.index(letter) + abs(shift)) % 26]
    else:
        new_letter = alfavit[(alfavit.index(letter) - abs(shift)) % 26]
    return new_letter


print(rotate_letter.__doc__)
print(rotate_letter.__annotations__)
print(rotate_letter('a', 3))

print(rotate_letter.__annotations__)
print(rotate_letter('d', -2))
