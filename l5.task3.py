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
# Точно так же как и получение элемента слева и extend слева.
# Что по сути весьма очевидно, потому что очередь для этого и нужна.

from collections import deque
from timeit import timeit


def lst_fulfill(num):
    lst = []
    for i in range(num):
        lst.append(i)
    return lst


def deq_fulfill(num):
    deq = deque()
    for i in range(num):
        deq.append(i)
    return deq


def lst_fulfill_left(num):
    lst = []
    for i in range(num):
        lst.insert(0, i)


def deq_fulfill_left(num):
    deq = deque()
    for i in range(num):
        deq.appendleft(i)


def lst_pop(lst):
    return lst.pop()


def deq_pop(deq):
    return deq.pop()


def lst_pop_left(lst):
    return lst.pop(0)


def deq_pop_left(deq):
    return deq.popleft()


def lst_extend_left(lst, lst2):
    lst = lst2 + lst
    return lst


def deq_extend_left(deq, deq2):
    deq.extend(deq2)
    return deq


print('Append')
print(timeit('lst_fulfill(10000)', number=10000, globals=globals()))
print(timeit('deq_fulfill(10000)', number=10000, globals=globals()))

print('Append left')
print(timeit('lst_fulfill_left(10000)', number=10000, globals=globals()))
print(timeit('deq_fulfill_left(10000)', number=10000, globals=globals()))

print('pop')
lst_a = lst_fulfill(30000)
deq_a = deq_fulfill(30000)
print(timeit('lst_pop(lst_a)', number=10000, globals=globals()))
print(timeit('deq_pop(deq_a)', number=10000, globals=globals()))

print('pop left')
lst_b = lst_fulfill(30000)
deq_b = deq_fulfill(30000)
print(timeit('lst_pop_left(lst_b)', number=10000, globals=globals()))
print(timeit('deq_pop_left(deq_b)', number=10000, globals=globals()))

print('extend left')
lst_c = lst_fulfill(30000)
deq_c = deq_fulfill(30000)
lst_d = lst_fulfill(100)
deq_d = deq_fulfill(100)
print(timeit('lst_extend_left(lst_c, lst_d)', number=1000, globals=globals()))
print(timeit('deq_extend_left(deq_c, deq_d)', number=1000, globals=globals()))

