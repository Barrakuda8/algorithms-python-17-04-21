"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

# Сделал доработку из подсказки. Сделал три пары замеров:
# - С уже отсортированным списком
# - С относительно большими случайными списками
# - С очень маленькими случайными спискоми
# В первом случае улучшенный алгоритм работает на порядок быстрее, в третьем улучшенный работает чуть быстрее,
# а во втором разницы почти нет. Связанно это с тем, что маленькие списки с гораздо большей вероятностью
# генерируются полностью или частично отсортированными, чем большие, а доработка расчитана как раз на такие случаи.
# Замеры с уже отсортированным списком показывают, что доработка действует.


from random import randint
from timeit import timeit


def create_rand_lst(num):
    return [randint(-100, 100) for _ in range(num)]


def sort_bubble(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


def better_sort_bubble(lst):
    n = 1
    while n < len(lst):
        sort_count = 0
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                sort_count = 1
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        if sort_count == 0:
            break
        n += 1
    return lst


lst1 = create_rand_lst(100)
print(lst1)
print(sort_bubble(lst1))
print(timeit('sort_bubble(lst1)', number=1000, globals=globals()))
print(timeit('better_sort_bubble(lst1)', number=1000, globals=globals()))

print(timeit('sort_bubble(create_rand_lst(100))', number=10000, globals=globals()))
print(timeit('better_sort_bubble(create_rand_lst(100))', number=10000, globals=globals()))

print(timeit('sort_bubble(create_rand_lst(5))', number=1000000, globals=globals()))
print(timeit('better_sort_bubble(create_rand_lst(5))', number=1000000, globals=globals()))

