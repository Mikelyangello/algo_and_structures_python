"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

rows = 5
columns = 4

matrix = []
for i in range(rows):
    row_arr = []
    for j in range(columns):
        elem = int(input(f'Введите значение на позицию {i+1}x{j+1} матрицы {rows}x{columns}: '))
        row_arr.append(elem)
    row_arr.append(sum(row_arr))
    matrix.append(row_arr)

for i in matrix:
    for j in range(columns):
        print(f'{i[j]:^3d}', end=' ')
    print(f'| {i[columns]:^3d}')
