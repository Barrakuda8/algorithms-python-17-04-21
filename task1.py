"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple


class Firm:

    def __init__(self):
        firm_data = namedtuple('Firm_Data', 'name income')
        self.data = firm_data(name=input('Введите название предприятия: '), income=self.income_input())

    def income_input(self):
        income = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split()
        if len(income) == 4:
            try:
                return sum(list(map(int, income)))
            except ValueError:
                pass
        self.income_input()


while True:
    try:
        firms_number = int(input('Введите количество предприятий для расчета прибыли: '))
        break
    except ValueError:
        continue

firms = []
average = 0

for i in range(firms_number):
    firm_i = Firm()
    firms.append(firm_i)
    average += firm_i.data.income

average = average / len(firms)
above_average = []
below_average = []

for i in firms:
    if i.data.income > average:
        above_average.append(i.data.name)
    else:
        below_average.append(i.data.name)

print(f'Средняя годовая прибыль всех предприятий: {average}')
print(f'Предприятия, с прибылью выше среднего значения: {above_average}')
print(f'Предприятия, с прибылью ниже среднего значения: {below_average}')
