# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple


def profit(x):
    average = (x.profit_1 + x.profit_2 + x.profit_3 + x.profit_4) / 4
    return average


count_firm = int(input('Введите количество фирм: '))
firm = namedtuple('firm', 'name, profit_1, profit_2, profit_3, profit_4, average')
database = {}
# Для тестирования
# database = {1: firm(name='Рога', profit_1=2.0, profit_2=2.0, profit_3=2.0, profit_4=2.0, average=2.0),
#             2: firm(name='Копыта', profit_1=4.0, profit_2=4.0, profit_3=4.0, profit_4=4.0, average=4.0),
#             3: firm(name='Рога и Копыта', profit_1=3.0, profit_2=3.0, profit_3=3.0, profit_4=3.0, average=3.0),
#             4: firm(name='И', profit_1=4.0, profit_2=5.0, profit_3=5.0, profit_4=5.0, average=5.0),
#             5: firm(name='Копыта и рога', profit_1=7.0, profit_2=7.0, profit_3=7.0, profit_4=7.0, average=7.0),
#             6: firm(name='и рога', profit_1=10.0, profit_2=10.0, profit_3=10.0, profit_4=10.0, average=10.0),
#             7: firm(name='Копыта и', profit_1=10.0, profit_2=10.0, profit_3=10.0, profit_4=10.0, average=10.0),
#             }
count = 1
while count <= count_firm:
    value = firm(str(input('Введите имя фирмы: ')),
                 float(input('Введите прибыль фирмы за 1-й квартал: ')),
                 float(input('Введите прибыль фирмы за 2-й квартал: ')),
                 float(input('Введите прибыль фирмы за 3-й квартал: ')),
                 float(input('Введите прибыль фирмы за 4-й квартал: ')), 0)
    value = value._replace(average=profit(value))
    database[count] = value
    count += 1
# данные по всем фирмам:
# for i in range(1, len(database) + 1):
#     print(f'Имя фирмы: {database[i].name}\n'
#           f' прибыль за 1-й квартал: {database[i].profit_1}\n'
#           f' прибыль за 2-й квартал: {database[i].profit_2}\n'
#           f' прибыль за 3-й квартал: {database[i].profit_3}\n'
#           f' прибыль за 4-й квартал: {database[i].profit_4}\n'
#           f' Средняя прибыль за год: {database[i].average}\n')

average_all = 0
for i in range(1, len(database) + 1):
    average_all += database[i].average
average_all = average_all / (len(database))

max_profit_id = []
min_profit_id = []

for i in range(1, len(database) + 1):
    if database[i].average >= average_all:
        max_profit_id.append(i)
    else:
        min_profit_id.append(i)

print('Прибыль равна или выше среднего у предприятий:')
for i in max_profit_id:
    print(database[i].name)

print('Прибыль ниже среднего у предприятий:')
for i in min_profit_id:
    print(database[i].name)
