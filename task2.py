"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""


# Замеры показали, что пузырьковый метод работает быстрее на списках размером меньше 20 элементов,
# после этого слияние работает быстрее и чем больше размер списка, тем существеннее разница в скорости.


from random import uniform
from timeit import timeit


def create_rand_lst(num):
    return [uniform(0, 50) for _ in range(num)]


def merge_sort(lst):
    if len(lst) < 2:
        return lst
    result = []
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    return result


# Пузырьковая сортировка из первого задания для сравнения
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


lst1 = create_rand_lst(10)
print(lst1)
print(merge_sort(lst1))
print(timeit('merge_sort(create_rand_lst(10))', number=10000, globals=globals()))
print(timeit('better_sort_bubble(create_rand_lst(10))', number=10000, globals=globals()))
print(timeit('merge_sort(create_rand_lst(100))', number=10000, globals=globals()))
print(timeit('better_sort_bubble(create_rand_lst(100))', number=10000, globals=globals()))
print(timeit('merge_sort(create_rand_lst(1000))', number=10000, globals=globals()))
print(timeit('better_sort_bubble(create_rand_lst(1000))', number=10000, globals=globals()))