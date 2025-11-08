"""
Перед вами вполне работающая функция get_extensions, которая принимает список названий файлов.
Функция get_extensions находит расширение у названий файлов и составляет из них список,
который возвращает в качестве ответа.
Если у файла нет расширения, то для такого файла get_extensions подставляет пустую строку.

Ваша задача — произвести рефакторинг данного кода для создания внутренней вспомогательной функции,
которая выполняет всю работу по поиску расширения. Вы можете, к примеру, назвать ее _get_extension и тогда,
определив такую функцию, ей можно пользоваться следующим образом:

for i in file_list:
    results.append(_get_extension(i))

или даже сразу так

return [_get_extension(i) for i in file_list]

Перепишите функцию get_extensions с учетом описанных пожеланий по созданию внутренней функции.
"""


def get_extensions(file_list):
    results = []

    def _get_extension(name):
        res = ""
        if "." in name:
            res = name.split(".")[-1]
        return res

    return [_get_extension(i) for i in file_list]

print(get_extensions(["foo.txt", "bar.mp4", "python3"]))
