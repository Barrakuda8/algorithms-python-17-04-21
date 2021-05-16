"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
__mul__
__add__
Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
1. вариант
defaultdict(list)
int(, 16)
reduce
2. вариант
class HexNumber:
    __add__
    __mul__
hx = HexNumber
hx + hx
hex()
"""

from collections import defaultdict

hex_dct = defaultdict(list, {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15})


def hex_check(lst):
    answer = []
    for i in lst:
        if hex_dct[i] != []:
            answer.append(i)
    return answer


def hex_number(lst):
    if len(lst) == 1:
        return hex_dct[lst[0]]
    else:
        return hex_dct[lst[0]] * (16 ** (len(lst) - 1)) + hex_number(lst[1:])


def dec_number(num):
    return hex(num)[2:].upper()


def hex_sum(hex1, hex2):
    return dec_number(hex_number(hex_check(hex1)) + hex_number(hex_check(hex2)))


def hex_mult(hex1, hex2):
    return dec_number(hex_number(hex_check(hex1)) * hex_number(hex_check(hex2)))


first = list(input('Введите первое шестнадцатиричное число: '))
second = list(input('Введите второе шестнадцатиричное число: '))
print(f'Сумма чисел равна: {list(hex_sum(first, second))}')
print(f'Произведение чисел равно: {list(hex_mult(first, second))}')



