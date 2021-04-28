"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Рекурсия вам нужна для решения левой части выражения.
Полученный результат нужно просто сравнить с результатом в правой.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Подсказка:
Правой части в рекурсии быть не должно. Необходимо сравнить результат, который даст рекурсивная ф-ция
со значением, полученным в правой части (здесь нужно просто подставить n и подсчитать)
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def rec_sum(num):
    if num == 1:
        return 1
    else:
        return rec_sum(num - 1) + num


def check(num):
    return rec_sum(num) == num * (num + 1)/2


# print(rec_sum(101))
# print(101 * (101 + 1)/2)
print(check(101))