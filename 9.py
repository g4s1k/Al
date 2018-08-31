#Найти максимальный элемент среди минимальных элементов столбцов матрицы


from random import randint


RANGE_START = 1
RANGE_END = 99
ROWS = 8
COLS = 6

matrix = [[randint(RANGE_START, RANGE_END) for _ in range(COLS)] for _ in range(ROWS)]

print('Заданная матрица: \n')

for item in matrix:
    print(*item)

print('-'*100)

mins = []
for col_num in range(COLS):
    min_el = matrix[0][col_num]
    for row_num in range(ROWS):
        if matrix[row_num][col_num] < min_el:
            min_el = matrix[row_num][col_num]
    mins +=[int(min_el)]
    if len(mins) > 1:
        buf = int(mins[0])
        if mins[col_num] > buf:
            mins[0] = int(mins[col_num])
            mins[col_num] = buf

print(f'Минимальные элементы столбцов матрицы: {mins} \nНаибольший из них: {mins[0]}') #Минимальные элементы перемешаны, чтобы не плодить еще цикл или буферную строку
