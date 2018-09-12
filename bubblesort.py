# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.


from random import randint


RANGE_START = -100
RANGE_END = 99
COUNT = 50

array = [randint(RANGE_START, RANGE_END) for _ in range(COUNT)]

print(f'Заданный массив: \n{array}\n')

def bubble_zero(array): # то, что хотели показать на уроке
    sorted_array = array[:]
    for i in range(0, COUNT - 1):
        for j in range(0, COUNT - 1):
            if sorted_array[j] < sorted_array[j + 1]:
                sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
                #print(f'Этап: \n{sorted_array}\n')
    return sorted_array

# py -3.6 -m timeit -n 30 -s "from bubblesort import bubble_zero, array" "bubble_zero(array)"
# COUNT = 10: 30 loops, best of 3: 13.4 usec per loop
# COUNT = 100: 30 loops, best of 3: 1.18 msec per loop
# COUNT = 1000: 30 loops, best of 3: 118 msec per loop
# O(N^2)

def bubble_one(array): # то, что показали на уроке
    sorted_array = array[:]
    for i in range(0, COUNT - 1):
        for j in range(0, COUNT - (i + 1)):
            if sorted_array[j] < sorted_array[j + 1]:
                sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
                #print(f'Этап: \n{sorted_array}\n')
    return sorted_array

# py -3.6 -m timeit -n 30 -s "from bubblesort import bubble_one, array" "bubble_one(array)"
# COUNT = 10: 30 loops, best of 3: 9.33 usec per loop
# COUNT = 100: 30 loops, best of 3: 775 usec per loop
# COUNT = 1000: 30 loops, best of 3: 76.3 msec per loop
# O(N^2)

def bubble_stone(array):  # надо было как-то оптимизировать....Встречайте: Пузырек и Камушек!!! xDDD
    sorted_array = array[:]
    for i in range(0, COUNT // 2):
        done = True
        for j in range(i, COUNT - (i + 1)):
            stone_j = COUNT - (j + 1) # иначе строка 43 выходила за рамки приличия и работало медленнее
            if sorted_array[j] < sorted_array[j + 1]:
                sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
                done = False
            if sorted_array[stone_j] > sorted_array[stone_j - 1]:
                sorted_array[stone_j], sorted_array[stone_j - 1] = sorted_array[stone_j - 1], sorted_array[stone_j]
                done = False
            #print(f'Этап: \n{sorted_array}\n')
        if done:
            break
    return sorted_array

# py -3.6 -m timeit -n 30 -s "from bubblesort import bubble_stone, array" "bubble_stone(array)"
# COUNT = 10: 30 loops, best of 3: 11 usec per loop
# COUNT = 100: 30 loops, best of 3: 958 usec per loop
# COUNT = 1000: 30 loops, best of 3: 96 msec per loop
# O(N^2)

# Я думал, будет быстрее за счет уменьшения количества итераций, однако дополнительная операция в цикле дала больший
# эффект. Но Пузырек и Камушек старались xD

stone_arr = bubble_stone(array)
print(f'Stone: \n{stone_arr}\n')

# if __name__ == "__main__":
#     assert bubble_zero(array) == bubble_one(array)
#     print('1 - OK')
#     assert bubble_one(array) == bubble_stone(array)
#     print('2 - OK')
