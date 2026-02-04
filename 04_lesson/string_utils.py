"""
Класс StringUtils для работы со строками
"""


class StringUtils:
    """
    Класс с методами для работы со строками
    """

    def capitilize(self, string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
        Пример: `capitilize("skypro") -> "Skypro"`
        """
        if not isinstance(string, str):
            raise TypeError("Input must be a string")

        if len(string) == 0:
            return string

        return string[0].upper() + string[1:]

    def trim(self, string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале, если они есть
        Пример: `trim("   skypro") -> "skypro"`
        """
        if not isinstance(string, str):
            raise TypeError("Input must be a string")

        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)

        return string

    def to_list(self, string: str, delimiter=",") -> list:
        """
        Принимает на вход текст с разделителем и возвращает список строк.
        Параметры:
            `string` - строка для обработки
            `delimiter` - разделитель строк. По умолчанию запятая (",")
        Пример 1: `to_list("a,b,c,d") -> ["a", "b", "c", "d"]`
        Пример 2: `to_list("1:2:3", ":") -> ["1", "2", "3"]`
        """
        if not isinstance(string, str):
            raise TypeError("Input must be a string")

        if len(string) == 0:
            return []

        return string.split(delimiter)

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка содержит искомый символ и `False` - если нет
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ
        Пример 1: `contains("SkyPro", "S") -> True`
        Пример 2: `contains("SkyPro", "U") -> False`
        """
        if not isinstance(string, str) or not isinstance(symbol, str):
            raise TypeError("Both arguments must be strings")

        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ для удаления
        Пример 1: `delete_symbol("SkyPro", "k") -> "SyPro"`
        Пример 2: `delete_symbol("SkyPro", "Pro") -> "Sky"`
        """
        if not isinstance(string, str) or not isinstance(symbol, str):
            raise TypeError("Both arguments must be strings")

        return string.replace(symbol, "")

    def starts_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка начинается с заданного символа и `False` - если нет
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ
        Пример 1: `starts_with("SkyPro", "S") -> True`
        Пример 2: `starts_with("SkyPro", "P") -> False`
        """
        if not isinstance(string, str) or not isinstance(symbol, str):
            raise TypeError("Both arguments must be strings")

        if len(symbol) == 0:
            return True

        return string.startswith(symbol)

    def end_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ
        Пример 1: `end_with("SkyPro", "o") -> True`
        Пример 2: `end_with("SkyPro", "y") -> False`
        """
        if not isinstance(string, str) or not isinstance(symbol, str):
            raise TypeError("Both arguments must be strings")

        if len(symbol) == 0:
            return True

        return string.endswith(symbol)

    def is_empty(self, string: str) -> bool:
        """
        Возвращает `True`, если строка пустая и `False` - если нет
        Пример 1: `is_empty("") -> True`
        Пример 2: `is_empty(" ") -> True`
        Пример 3: `is_empty("SkyPro") -> False`
        """
        if not isinstance(string, str):
            raise TypeError("Input must be a string")

        return len(string.strip()) == 0

    def list_to_string(self, lst: list, joiner=", ") -> str:
        """
        Преобразует список элементов в строку с указанным разделителем
        Параметры:
            `lst` - список элементов
            `joiner` - разделитель. По умолчанию запятая (", ")
        Пример 1: `list_to_string([1,2,3,4]) -> "1, 2, 3, 4"`
        Пример 2: `list_to_string(["Sky", "Pro"]) -> "Sky, Pro"`
        Пример 3: `list_to_string(["Sky", "Pro"], "-") -> "Sky-Pro"`
        """
        if not isinstance(lst, list):
            raise TypeError("First argument must be a list")

        if not isinstance(joiner, str):
            raise TypeError("Joiner must be a string")

        string_list = [str(item) for item in lst]
        return joiner.join(string_list)