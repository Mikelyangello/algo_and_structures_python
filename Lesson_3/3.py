# 3. В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import random

any_arr = []

# создаем массив со случайным количеством случайных целых чисел
for i in range(int(random() * 100) + 1):
    # сначала писал вариант для неповторяющихся чисел, но условия работают для любых массивов (ищется первое вхождение)
    # any_number = int(random() * 100)
    # if any_number not in any_arr:
    #     any_arr.append(any_number)
    any_arr.append(int(random() * 100))

# присваиваем переменным значение первого элемента массива
max_number = any_arr[0]
min_number = any_arr[0]

print(f'До замены массив имеет вид: {any_arr}\n')

# проходимся по всему массиву и записываем максимальные и минимальные значения среди элементов
for i in any_arr:
    if i > max_number:
        max_number = i
    if i < min_number:
        min_number = i

# сохраняем в переменную индекс максимального элемента до изменений
max_number_index_original = any_arr.index(max_number)

# меняем элементы местами
any_arr[any_arr.index(min_number)] = max_number
any_arr[max_number_index_original] = min_number

print(f'Замена в массиве произведена, '
      f'{max_number}[{max_number_index_original + 1}] на '
      f'{min_number}[{any_arr.index(max_number) + 1}]:\n'
      f'массив после внесения изменений:\n'
      f'{any_arr}')
