# Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков


from random import randint
from cProfile import run


IN_ARRAY = [10, 5, 3, 8, 15, 11, 3, 1]
OUT_ARRAY = [10, 5, 3, 8, 1, 11, 3, 15]

def generate_array(range_start = 1, range_end = 99, count = 10):
    #выдает массив случайных чисел с заданными параметрами и значения параметров

    array = [randint(range_start, range_end) for _ in range(count)]
    min_possible_el = range_start
    max_possible_el = range_end
    array_len = count

    return array, min_possible_el, max_possible_el, array_len

def min_max_changer(array, min_possible_el, max_possible_el, array_len):
    # меняет местами наибольший и наименьший элементы массива, ничего лишнего

    max_element_info = [0, min_possible_el - 1]
    min_element_info = [0, max_possible_el + 1]

    for index in range(array_len):
        if array[index] > max_element_info[1]:
            max_element_info = [index, array[index]]
        if array[index] < min_element_info[1]:
            min_element_info = [index, array[index]]

    array[max_element_info[0]] = min_element_info[1]
    array[min_element_info[0]] = max_element_info[1]

    return array

def test_min_max_changer(): # тест

    min_pos_el = min(IN_ARRAY)
    max_pos_el = max(IN_ARRAY)
    array_len = len(IN_ARRAY)

    assert min_max_changer(IN_ARRAY, min_pos_el, max_pos_el, array_len) == OUT_ARRAY
    print('TEST DONE')

data = generate_array(count = 10000) # генерируем массив для теста


# Строка вызова timeit: python -m timeit -n 1000 -s "from myanalyse import data, min_max_changer" "min_max_changer(*data)"
# результат с count = 100: 1000 loops, best of 5: 15.5 usec per loop
# результат с count = 1000: 1000 loops, best of 5: 154 usec per loop
# результат с count = 10000: 1000 loops, best of 5: 1.48 msec per loop

# Интересно, что при линейной сложности и, в общем-то небольшом времени выполнения согласно последнему результату timeit
# комп довольно долго тупил, я решил посмотреть генерацию.

# запрос: python -m timeit -n 1000 -s "from myanalyse import generate_array" "generate_array(count = 100)"
# результат: 1000 loops, best of 5: 94.5 usec per loop

# запрос: python -m timeit -n 1000 -s "from myanalyse import generate_array" "generate_array(count = 1000)"
# результат: 1000 loops, best of 5: 961 usec per loop

# запрос: python -m timeit -n 1000 -s "from myanalyse import generate_array" "generate_array(count = 10000)"
# результат: 1000 loops, best of 5: 9.57 msec per loop

# Тут я ждал секунд 30 или даже больше, хотя сложность линейная и время выполнения функции 9.5 мкс. Дело в подготовке
# ресурсов? А что будет, если так тестировать алгоритмысерьезных объемах данных?

# Теперь переходим к профилированию:


if __name__ == '__main__':
    test_min_max_changer()
    run('min_max_changer(*data)')


#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 myanalyse.py:22(min_max_changer)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Интересно, что exec выполняется в 2 раза дольше, чем исследуемая функция.
