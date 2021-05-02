"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""

# Я не нашёл информации о том какой сложности является функция str(), но логически это либо линейная, либо константная.
# Этого хватит для аналитики этого задания, хотя хотелось бы узнать, какая всё-таки у неё сложность, пожалуйста с:
# Для простоты, в этом задании говорю об str() как о линейной, потому что во-первых я всё же склоняюсь к этому варианту,
# А во вторых это бОльшая из двух.

# Самый эффективный вариант - через срез (3), что вполне логично,
# потому что в данной функции всего две операции, обе линейные и простые.
# Вариант через reverse() (5) на втором месте по скорости. Тут уже 4 линейные операции, но всё ещё простые.
# На третьем - вариант через цикл (2). Цикл ещё и с набором математических операций,
# поэтому медленнее простых вариантов выше, но быстрее рекурсий ниже
# Рекурсия данная в задании (1) выполняется немного быстрее, чем моя рекурсия (4), потому что в ней нет
# постоянных конвертаций чисел в строку и наоборот, а всегда происходит работа только с числами.

from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def reverse_4(num):
    if num // 10 == 0:
        return num % 10
    else:
        return f'{num % 10}{reverse_4(num // 10)}'


def reverse_5(num):
    num = list(str(num))
    num.reverse()
    return ''.join(num)


print(timeit('revers_1(1234567890)', globals=globals()))
print(timeit('revers_2(1234567890)', globals=globals()))
print(timeit('revers_3(1234567890)', globals=globals()))
print(timeit('reverse_4(1234567890)', globals=globals()))
print(timeit('reverse_5(1234567890)', globals=globals()))
run('revers_1(1234567890)')
run('revers_2(1234567890)')
run('revers_3(1234567890)')
run('reverse_4(1234567890)')
run('reverse_5(1234567890)')
