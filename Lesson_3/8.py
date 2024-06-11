"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

matrix = []
maximum = 0

for i in range(5):
    b = []
    row_sum = 0
    for j in range(4):
        new_el = int((input(f"Input element in matrix your position now: row-{i+1} col-{j+1}: ")))
        row_sum += new_el
        b.append(new_el)

    b.append(row_sum)
    maximum = maximum if maximum > row_sum else row_sum
    matrix.append(b)

maximum = len(str(maximum)) + int(len(str(maximum)) / 2)

for i in matrix:
    for j in i:
        print(f"{j:<{maximum}}", end='')
    print()
