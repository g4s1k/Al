# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы


from random import randint


RANGE_START = 1
RANGE_END = 99
COUNT = 10

array = [randint(RANGE_START, RANGE_END) for _ in range(COUNT)]
max_element_info = [0, RANGE_START - 1]
min_element_info = [0, RANGE_END + 1]

for index in range(COUNT):
    if array[index] > max_element_info[1]:
        max_element_info = [index, array[index]]
    if array[index] < min_element_info[1]:
        min_element_info = [index, array[index]]

print(f'Заданный массив: \n{array}\n')

array[max_element_info[0]] = min_element_info[1]
array[min_element_info[0]] = max_element_info[1]

print(f'Измененный массив: \n{array}\n')

#Думаю, что можно было бы сделать поэкономнее вов сех смыслах этого слова, однако опять делаю в последний момент :/
