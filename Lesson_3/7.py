"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import random

any_arr = []

# создаем массив со случайным количеством случайных целых чисел с наличием отрицательных значений
for i in range(int(random() * 100) + 1):
    if random() > 0.5:
        any_arr.append(int(random() * 100))
    else:
        any_arr.append(int(random() * (-100)))

# присваиваем переменной значение первого элемента массива
min_number1 = any_arr[0]

# находим первое минимальное значение в массиве
for i in any_arr:
    if i < min_number1:
        min_number1 = i

# проверяем - находится ли минимальное значение в начале массива и создаем соответствующие переменные с индексом
if min_number1 == any_arr[0]:
    min_number2 = any_arr[1]
    min_number2_index = 1
else:
    min_number2 = any_arr[0]
    min_number2_index = 0

cur_index = 0

for i in any_arr:
    if i < min_number2 and cur_index != any_arr.index(min_number1):
        min_number2 = i
        min_number2_index = cur_index + 1
    cur_index += 1

print(f'\nВ массиве {any_arr}\n'
      f'Есть 2 минимальных элемента:\n'
      f'№1 = {min_number1}[{any_arr.index(min_number1) + 1}]\n'
      f'№2 = {min_number2}[{min_number2_index}]')
