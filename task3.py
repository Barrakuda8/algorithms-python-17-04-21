"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...
[5, 3, 4, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 4, 5]
my_lst
new_lts
arr[m]
from statistics import median
[3, 4, 3, 3, 5, 3, 3]
left = []
right = []
left == right and
for i in
    for
    left == right
    left.clear()
    right.clear()
"""


def median(lst):
    half = len(lst)//2
    smaller = []
    bigger = []
    m = lst[0]
    for i in lst:
        if i > m:
            bigger.append(i)
            if len(bigger) >= half:
                smaller.append(m)
                m = min(bigger)
                bigger.remove(m)
        elif i < m:
            smaller.append(i)
            if len(smaller) >= half:
                bigger.append(m)
                m = max(smaller)
                smaller.remove(m)
    return m


print(median([3, 3, 3, 3, 3, 4, 5]))
