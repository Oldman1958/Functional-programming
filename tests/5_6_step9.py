"""
Перед вами частично реализованная функция double_odd_numbers,
которая принимает список чисел и возвращает в качестве результата новый список,
составленный из нечетных чисел, увеличенных в два раза.

Внутри себя double_odd_numbers использует две функции:

double, увеличивающая число в два раза;

is_odd, проверяющая на нечетность
Ваша задача реализовать эти функции внутри  double_odd_numbers
"""


def double_odd_numbers(numbers):
    def double(x):
        return 2 * x

    def is_odd(x):
        return True if x % 2 != 0 else False

    return [double(num) for num in numbers if is_odd(num)]


print(double_odd_numbers([1, 2, 3, 4, 5]))

print(double_odd_numbers([6, 8, 10, 2]))

print(double_odd_numbers([-43, 91, 932, 9201, 32, 93]))
