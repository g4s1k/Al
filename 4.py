# Определить, какое число в массиве встречается чаще всего


from random import randint


RANGE_START = 1
RANGE_END = 99
COUNT = 16

array = [randint(RANGE_START, RANGE_END) for _ in range(COUNT)]

print(f'Заданный массив: \n{array}\n')

for out_index in range(COUNT):
    element = array[out_index]
    count = 1
    if element > RANGE_START - 1:
        for in_index in range(out_index + 1, COUNT):
            if (array[in_index] > RANGE_START - 1) and (array[in_index] == element):
                count += 1
                array[in_index] = RANGE_START - 1
        array[out_index] = (element, count)

ans = (RANGE_START - 1, 1)

for element in array:
    if element != RANGE_START - 1:
        if element[1] > ans [1]:
            ans = element

if ans[0] > RANGE_START - 1:
    print(f'Чаще всего в заданном массиве встречается число {ans[0]}, а именно, {ans[1]} раз(а).')
else:
    print('Все числа встречаются в массиве один раз')

#В условиях цайтнота порой рождаются поразительные вещи.... @.@
