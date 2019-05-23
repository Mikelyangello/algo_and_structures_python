"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import random

any_arr = []

# создаем массив со случайным количеством случайных целых чисел
for i in range(int(random() * 100) + 1):
    any_arr.append(int(random() * 100))

# присваиваем переменным значение первого элемента массива
max_number = any_arr[0]
min_number = any_arr[0]

# проходимся по всему массиву и записываем максимальные и минимальные значения среди элементов
for i in any_arr:
    if i > max_number:
        max_number = i
    if i < min_number:
        min_number = i

# создаем переменную результата, флаг(маркер) целевой зоны и индекс
result = 0
flag_glob = False
cur_index = 0

for i in any_arr:
    # если наш элемент является минимальным или максимальным значением в массиве, срабатывает локальный флаг
    flag_curr = cur_index == any_arr.index(min_number)\
                or cur_index == any_arr.index(max_number)
    if flag_curr:
        flag_glob = not flag_glob
    # проверяем состояние глобального флага и флага положения на макс/мин элементе
    if flag_glob and not flag_curr:
        result += i
    cur_index += 1

print(f'Сумма элементов между '
      f'{min_number}[{any_arr.index(min_number) + 1}] и '
      f'{max_number}[{any_arr.index(max_number) + 1}]\n'
      f'массива\n{any_arr}\nравна {result}')
