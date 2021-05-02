"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""

# Оказывается list comprehension работает медленнее обычного цикла, интересно.
# Оптимизированный вариант - func_4. По сути я просто совместил индексы и элементы от индексов в enumerate объекте,
# что видимо ускорило работу, потому что каждый раз находить элемент по индексу дольше, чем один раз использовать
# enumerate().

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    return [i for i, j in enumerate(nums) if j % 2 == 0]


def func_4(nums):
    new_arr = []
    for i, j in enumerate(nums):
        if j % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit("func_1([1, 3, 1, 3, 4, 5, 1])", globals=globals()))
print(timeit("func_2([1, 3, 1, 3, 4, 5, 1])", globals=globals()))
print(timeit("func_3([1, 3, 1, 3, 4, 5, 1])", globals=globals()))
print(timeit("func_4([1, 3, 1, 3, 4, 5, 1])", globals=globals()))