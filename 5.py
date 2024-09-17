#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве


from random import randint


RANGE_START = -99 #MUST BE NEGATIVE!
RANGE_END = 99
COUNT = 20

array = [randint(RANGE_START, RANGE_END) for _ in range(COUNT)]

print(f'Заданный массив: \n{array}\n')

max_negative_el = (-1, RANGE_START - 1)

for index in range(COUNT):
    if (array[index] < 0) and (array[index] > max_negative_el[1]):
        max_negative_el = (index, array[index])

if max_negative_el[0] > -1:
    print(f'Наибольший отрицательный элемент в массиве - это элемент под номером {max_negative_el[0]} '
          f'равный {max_negative_el[1]}')
else:
    print('Все элементы массива - неотрицательные числа') #а то мало ли там нарандомит
