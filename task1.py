"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

# Заполнение словаря на очень больших числах выполняется медленее, чем заполнение списка.
# Однако остальные функции во много раз, а то и на несколько порядков, быстрее.
# Связанно это с тем, что при заполнении словаря происходит хэширование данных,
# что помогает обращаться к его элементам сразу по ключам, в то время как в случае со списком,
# этот процесс занимает куда больше времени, потому что запрашиваемый элемент приходится искать перебором.


from time import perf_counter


def time_measure(func):
    def measure(x, num):
        start = perf_counter()
        for _ in range(num):
            func(x)
        end = perf_counter()
        print(f'{func} - {end - start}')
    return measure


@time_measure
def fulfill_lst(lst):
    for i in range(1000000):
        lst.append(i)


@time_measure
def fulfill_dct(dct):
    for i in range(1000000):
        dct[i] = i


@time_measure
def delete_lst(lst):
    for i in range(100000):
        lst.remove(i)


@time_measure
def delete_dct(dct):
    for i in range(100000):
        del dct[i]


@time_measure
def pop_lst(lst):
    return lst.pop()


@time_measure
def pop_dct(dct):
    for i in range(200000, 300000):
        return dct.pop(i)


@time_measure
def search_lst(lst):
    return 400000 in lst


@time_measure
def search_dct(dct):
    return 400000 in dct


lst_a = []
for i in range(1000000):
    lst_a.append(i)

dct_a = {}
for i in range(1000000):
    dct_a[i] = i

fulfill_lst([], 10000)
fulfill_dct({}, 10000)
delete_lst(lst_a, 1)
delete_dct(dct_a, 1)
pop_lst(lst_a, 100000)
pop_dct(dct_a, 1)
search_lst(lst_a, 1000)
search_dct(dct_a, 1000)