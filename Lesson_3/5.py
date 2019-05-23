#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import random

any_arr = []

# создаем массив со случайным количеством случайных целых чисел с наличием отрицательных значений
for i in range(int(random() * 100) + 1):
    if random() > 0.5:
        any_arr.append(int(random() * 100))
    else:
        any_arr.append(int(random() * (-100)))

# присваиваем переменным значение первого элемента массива и его позиции
max_negativ_number = any_arr[0]
max_negativ_number_position = 1

# находим и записываем в переменную самый маленький элемент массива
for i in any_arr:
    if i < max_negativ_number:
        max_negativ_number = i

# перебираем все элементы и записываем в переменную тот, что подходит по условиям
for i in any_arr:
    if max_negativ_number < i < 0:
        max_negativ_number = i
        max_negativ_number_position = any_arr.index(i) + 1

print(f'\nв массиве {any_arr}\nмаксимальный отрицательный элемент {max_negativ_number}[{max_negativ_number_position}]')
