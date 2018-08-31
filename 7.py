#В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться


from random import randint


RANGE_START = 0
RANGE_END = 99
COUNT = 10

array = [randint(RANGE_START, RANGE_END) for _ in range(COUNT)]

print(f'Заданный массив: \n{array}\n')

for out_ind in range(2):
    for index in range(out_ind, COUNT):
        if array[index] < array[out_ind]:
            buf = int(array[out_ind])
            array[out_ind] = int(array[index])
            array[index] = buf

if array[0] != array[1]:
    print(f'Пара наименьших значений массива: {array[0]}, {array[1]}\n')
else:
    print(f'Оба наименьших элементов массива равны между собой, их значение равно: {array[0]}')
