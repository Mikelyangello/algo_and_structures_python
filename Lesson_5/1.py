"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""


# Пока работа над ДЗ в процессе. Буде обновлять  PR. Как только закончу - удалю этот комментарий

import collections

count_of_corps = int(input('Введите количество оцениваемых предприятий\n'))
corporations = collections.defaultdict(list)
summ_of_profit = 0

for i in range(count_of_corps):
    corp_name = input(f'Введите название предприятия №{i+1}\n')
    for j in range(4):
        corporations[corp_name].append(int(input(f'Введите прибыль компании "{corp_name}" за {j+1}й квартал: ')))
    summ_of_profit += sum(corporations[corp_name])

avg_profit = summ_of_profit / count_of_corps

for k, v in corporations.items():
    profit = sum(v)
    if profit < avg_profit:
        print(f'У компании {k} прибыль за год {v} в размере {profit} ниже среднего ({avg_profit:.1f})')
    else:
        print(f'У компании {k} прибыль за год {v} в размере {profit} выше среднего ({avg_profit:.1f})')

