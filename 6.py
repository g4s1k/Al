#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать


from random import randint


RANGE_START = -99
RANGE_END = 99
COUNT = 10

array = [randint(RANGE_START, RANGE_END) for _ in range(COUNT)]
sum = 0

print(f'Заданный массив: \n{array}\n')

max_el = (0, RANGE_START - 1)
min_el = (0, RANGE_END + 1)

for index in range(COUNT):
    if array[index] >= max_el[1]:                  #тут добавил оператор равенства, чтобы взять крайние элементы
        max_el = (index, array[index])
    if array[index] <= min_el[1]:
        min_el = (index, array[index])

distance = abs(max_el[0] - min_el[0])
if distance > 1:
    if max_el[0] < min_el[0]:
        first = max_el[0]
    else:
        first = min_el[0]

    for index in range(first + 1, first + distance):
        sum += array[index]

    print('-' * 100, '\n'*2,'Сумма равна:', sum)

else:
    print('Выпали соседние элементы >:|')
