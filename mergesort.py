# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

# Ломал голову, как реализовать покрасивше, голова сломалась, после чего пришлось скатать алгоритм с википедии :((


from random import uniform
from collections import deque


RANGE_START = 0
RANGE_END = 50
COUNT = 15

array = []
for _ in range(COUNT):
    num = uniform(RANGE_START, RANGE_END)
    if num != 50.0:
        array.append(num)

def merge_sort(array):
    def merge(left, right):
        result = deque()
        while left and right:
            if left[-1] >= right[-1]:
                result.appendleft(left.pop())
            else:
                result.appendleft(right.pop())
        while left:
            result.appendleft(left.pop())
        while right:
            result.appendleft(right.pop())
        return list(result)

    array_len = len(array)
    middle = array_len // 2

    if array_len <= 1:
        return array
    else:
        left = array[: middle]
        right = array[middle : array_len]

        left = merge_sort(left)
        right = merge_sort(right)
        result = merge(left, right)

        return result

if __name__ == '__main__':
    sorted_array = merge_sort(array)
    print(f'Заданный массив: \n{array}\n')
    print(f'Полученный массив: \n{sorted_array}\n')
