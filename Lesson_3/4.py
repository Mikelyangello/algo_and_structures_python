# 4.	Определить, какое число в массиве встречается чаще всего.

from random import random

any_arr = []

# создаем массив со случайным количеством случайных целых чисел
for i in range(int(random() * 100) + 1):
    any_arr.append(int(random() * 100))

max_count = 0
number_with_max_counter = any_arr[0]

for i in any_arr:
    counter = 0
    for j in any_arr:
        if j == i:
            counter += 1
    if counter > max_count:
        max_count = counter
        number_with_max_counter = i

print(f'\nв массиве {any_arr}\nчаще всего встречается число {number_with_max_counter}({max_count} раз)')
