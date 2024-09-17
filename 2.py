# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа


from random import randint


RANGE_START = 1
RANGE_END = 99
COUNT = 10

array = [randint(RANGE_START, RANGE_END) for _ in range(COUNT)]
ans = []

for index in range(COUNT):
    if array[index] % 2 == 0:
        ans += [index]

print(f'Полученный массив: \n{array}\n')
print(f'Индексы четных элементов: \n{ans}')
