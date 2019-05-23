# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

rows = int(random() * 5) + 5
columns = int(random() * 5) + 5

matrix = []
for i in range(rows):
    row_arr = []
    for j in range(columns):
        elem = int(random() * 100)
        row_arr.append(elem)
    matrix.append(row_arr)

for i in matrix:
    for j in range(columns):
        print(f'{i[j]:^3d}', end=' ')
    print('')

min_arr = []

for i in matrix:
    min_elem = i[0]
    for j in i:
        if j < min_elem:
            min_elem = j
    min_arr.append(min_elem)

max_elem = min_arr[0]

for i in min_arr:
    if i > max_elem:
        max_elem = i

print(f'\nМаксимальный элемент среди минимальных элементов столбцов ({min_arr}) матрицы: {max_elem}')
