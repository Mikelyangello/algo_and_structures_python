# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
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
min_els = []

for i in matrix:
    for j in i:
        print(f"{j:<{maximum}}", end='')
    print()

for j in range(len(matrix)):
    m = None
    for i in range(len(matrix[j])):
        m = matrix[i][j] if m is None else m
        m = matrix[i][j] if m > matrix[i][j] else m
    min_els.append(m)


print(f"Минимальные элементы столбцов матрицы: {min_els}, среди них максимум:\n{max(min_els)}")
