"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def main(str_1: str, str_2: str) -> int:
    if not (isinstance(str_1, str) and isinstance(str_2, str)):
        return 0
    elif str_1 == str_2:
        return 1
    elif (str_1 != str_2) and (len(str_1) > len(str_2)) and str_2 != 'learn':
        return 2
    elif (str_1 != str_2) and str_2 == 'learn':
        return 3
    else:
        pass


if __name__ == "__main__":
    test_list = [(25, 'qwerty'), ('qwerty', 'qwerty'),
                 ('qwerty', 'ytrew'), ('qwerty', 'learn'), ('qwerty', 'qwertyu')]
    for (str_1, str_2) in test_list:
        print(main(str_1, str_2))
