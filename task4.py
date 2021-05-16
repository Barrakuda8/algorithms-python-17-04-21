"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым из них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

# Операция заполнения словаря выполняется быстрее заполнения OrderedDict, видимо засчёт того, что последний ещё
# закрепляет последовательность дополнительно. Остальные операции выполняются примерно одинаково.
# Вывод: исходя из этих операций, OrderedDict не нужен, что логично, потому что его дополнительный, по сравнению
# с обычным словарём, функционал - больше не дополнительный и по сути устаревший.

from collections import OrderedDict
from timeit import timeit


def dct_fulfill():
    dct = dict()
    for i in range(100000):
        dct[i] = i
    return dct


def ord_fulfill():
    ord = OrderedDict()
    for i in range(100000):
        ord[i] = i
    return ord


def dct_get(dct):
    return dct[500]


def ord_get(ord):
    return ord[500]


def dct_search(dct):
    return 500 in dct


def ord_search(ord):
    return 500 in ord


dct_a = dct_fulfill()
ord_a = ord_fulfill()
print(timeit('dct_fulfill()', number=10000, globals=globals()))
print(timeit('ord_fulfill()', number=10000, globals=globals()))
print(timeit('dct_get(dct_a)', number=100000000, globals=globals()))
print(timeit('ord_get(ord_a)', number=100000000, globals=globals()))
print(timeit('dct_search(dct_a)', number=100000000, globals=globals()))
print(timeit('ord_search(ord_a)', number=100000000, globals=globals()))