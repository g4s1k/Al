# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше ее.

# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках.


from random import randint
from mergesort import merge_sort # для проверки в конце


RANGE_START = 0
RANGE_END = 5
MM = 5

array = [randint(RANGE_START, RANGE_END) for _ in range(2*MM + 1)]

print(f'Заданный массив: \n{array}\n')

def findmediane(array):
    for sample in array:
        less_count = 0
        greater_count = 0
        equal_count = -1
        for element in array:
            if element is not sample:
                if element > sample:
                    greater_count += 1
                else:
                    less_count += 1
            else:
                equal_count += 1
        if equal_count >= abs(less_count - greater_count):
            return sample

mediane = findmediane(array)
sorted_array = merge_sort(array)
mediane_from_sorted = sorted_array[((2*MM + 1) // 2)]
print(f'Отсортированный массив: \n{sorted_array}')
print(f'Нашли медиану: {mediane}')
print(f'Результат: {mediane == mediane_from_sorted}')
