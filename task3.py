"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача:
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""

# Заполнение списка и очереди происходит с одинаковой скорость, получение последнего элемента тоже.
# Заполнение очереди слева выполняется во много раз быстрее заполнения слева списка.
# Что по сути весьма очевидно, потому что очередь для этого и нужна.

from collections import deque
from timeit import timeit


def lst_fulfill():
    lst = []
    for i in range(100000):
        lst.append(i)
    return lst


def deq_fulfill():
    deq = deque()
    for i in range(100000):
        deq.append(i)
    return deq


def lst_fulfill_left():
    lst = []
    for i in range(10000):
        lst.insert(0, i)


def deq_fulfill_left():
    deq = deque()
    for i in range(10000):
        deq.appendleft(i)


def lst_pop(lst):
    return lst.pop()


def deq_pop(deq):
    return deq.pop()


lst_a = lst_fulfill()
deq_a = deq_fulfill()
print(timeit('lst_fulfill()', number=10000, globals=globals()))
print(timeit('deq_fulfill()', number=10000, globals=globals()))
print(timeit('lst_fulfill_left()', number=10000, globals=globals()))
print(timeit('deq_fulfill_left()', number=10000, globals=globals()))
print(timeit('lst_pop(lst_a)', number=100000, globals=globals()))
print(timeit('deq_pop(deq_a)', number=100000, globals=globals()))