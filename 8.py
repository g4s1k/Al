#Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу


COLS = 5
ROWS = 4

matrix = [0 for _ in range(ROWS)]

for index in range(ROWS):
    buf = []
    sum_ = 0
    for item in input(f'Введите через пробел первые {COLS - 1} элемента(ов) {index + 1}й строки матрицы: \n').split(' '): #щепотка пайтон стайла
        buf += [int(item)]
        sum_ += int(item)
    buf += [sum_]
    matrix[index] = buf

print('-'*100)

for index in range(ROWS):
    print(*matrix[index])
