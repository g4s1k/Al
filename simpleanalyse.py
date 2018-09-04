# Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.

# Я сначала неправильно понял задачу и написал 3 функции нахождения простых чисел в последовательности из n целых чисел.
# Некоторый комментарий относительно моих соображений приведен после секции с данными функциями


from cProfile import run


def erat_alh_power(n):
    num_list = [num for num in range(2, n + 1)]              # < - Выписываем на дощечку все целые числа от 2 до n
    p = 2                                                    # < - первое простое число
    while True:                                              # < - пока не дойдем до последнего числа в качестве делителя
        for index in range(2*p - 2, n - 1, p):
            num = num_list[index]
            if (num > p) and (num != 0) and (num % p == 0):  # Протыкаем числа на каждый p-й шаг, начиная с 2p
                num_list[index] = 0
        if 2*p > n:
            break
        for index in range(p-2, n - 1):
            num = num_list[index]
            if (num > p) and (num != 0):                     # Все числа до p включительно или обведены, или проткнуты.
                p = num                                      # Мы видим первое непроткнутое число после p и берем его
                break                                        # в качестве нового делителя.

    return num_list                                          # На выходе дощечка с простыми числами


# Строка вызова timeit: python -m timeit -n 100 -s "from simpleanalyse import erat_alh_power" "erat_alh_power(100)"
# результат 100 loops, best of 5: 26.8 usec per loop
# Строка вызова timeit: python -m timeit -n 100 -s "from simpleanalyse import erat_alh_power" "erat_alh_power(1000)"
# результат 100 loops, best of 5: 286 usec per loop
# Строка вызова timeit: python -m timeit -n 100 -s "from simpleanalyse import erat_alh_power" "erat_alh_power(10000)"
# результат 100 loops, best of 5: 2.94 msec per loop

# Линейная сложность


def upgraded_erat_alh(n):
    num_list = [num for num in range(2, n + 1)]
    p = 2
    while True:

        if p == 2:
            inc = p
        else:
            inc = 2*p

        for index in range(p**2 - 2, n - 1, inc):
            num = num_list[index]
            if (num != 0) and (num % p == 0):
                num_list[index] = 0

        index = p - 2

        if p == 2:
            inc = 1
        else:
            inc = 2

        while (index < n - 1):
            index += inc
            num = num_list[index]
            if num != 0:
                p = num
                break

        if p**2 > n:
            break
    return num_list


# Строка вызова timeit: python -m timeit -n 100 -s "from simpleanalyse import upgraded_erat_alh" "upgraded_erat_alh(100)"
# результат 100 loops, best of 5: 12.9 usec per loop
# Строка вызова timeit: python -m timeit -n 100 -s "from simpleanalyse import upgraded_erat_alh" "upgraded_erat_alh(1000)"
# результат 100 loops, best of 5: 131 usec per loop
# Строка вызова timeit: python -m timeit -n 100 -s "from simpleanalyse import upgraded_erat_alh" "upgraded_erat_alh(10000)"
# результат 100 loops, best of 5: 1.35 msec per loop

# Линейная сложность, примерно в 2 раза быстрее


def simple_power(n):
    num_list = [num for num in range(2, n + 1)]
    begin = 1
    end = n - 1
    while begin <= end:
        p = num_list[begin - 1]
        index = begin
        while index < end:
            if num_list[index] % p == 0:
                del(num_list[index])
                end -= 1
            else:
                index += 1
        begin += 1

    return num_list

# Строка вызова timeit: python -m timeit -n 100 -s "from simpleanalyse import simple_power" "simple_power(100)"
# результат 100 loops, best of 5: 44.8 usec per loop
# Строка вызова timeit: python -m timeit -n 100 -s "from simpleanalyse import simple_power" "simple_power(1000)"
# результат 100 loops, best of 5: 1.47 msec per loop
# Строка вызова timeit: python -m timeit -n 100 -s "from simpleanalyse import simple_power" "simple_power(10000)"
# результат 100 loops, best of 5: 83.1 msec per loop

# Сложность явно не линейная на мое удивление, я думал, что так будет быстрее....Короткое - не всегда быстрое


# И вот тут я понял, что делаю немного не то........
# Согласно Википедии "Решето́ Эратосфе́на — алгоритм нахождения всех простых чисел до некоторого целого числа n"
# И лично мне совершенно непонятно, как можно реализовать с помощью этого алгоритма задачу вычисления i-го простого числа,
# так как необходимо знать, сколько конкретно нужно перебрать целых чисел, чтобы получить i-е простое число.
# Однако, если отступить от метода решета Эратосфена в чистом виде, то можно реализовать данную задачу, хотя и не очень
# эффективно.

# Первый приходящий на ум алгоритм, не похожий на решето:

def find_i_simple_num(i):
    count = 1
    num = 2
    simple_list = [2]
    while count < i:
        num += 1
        flag = True
        for item in simple_list:
            if num % item == 0:
                flag = False
        if flag:
            simple_list.append(num)
            count += 1
    return simple_list[i - 1]

# Строка вызова timeit: python -m timeit -n 100 -s "from simpleanalyse import find_i_simple_num" "find_i_simple_num(10)"
# результат 100 loops, best of 5: 9.8 usec per loop
# Строка вызова timeit: python -m timeit -n 100 -s "from simpleanalyse import find_i_simple_num" "find_i_simple_num(100)"
# результат 100 loops, best of 5: 1.2 msec per loop
# Строка вызова timeit: python -m timeit -n 100 -s "from simpleanalyse import find_i_simple_num" "find_i_simple_num(1000)"
# результат 100 loops, best of 5: 192 msec per loop

# Естественно, сложность нелинейная. Я думал при последнем запуске я не дождусь ответа.
# Однако, как мне кажется, работает весьма шустро для такой задачи

# В интервале от 2 до 100 находится 25 простых чисел, сравним производительность Эратосфена с простым перебором:

# Строка вызова timeit: python -m timeit -n 100 -s "from simpleanalyse import find_i_simple_num" "find_i_simple_num(25)"
# результат 100 loops, best of 5: 63.5 usec per loop
# Строка вызова timeit: python -m timeit -n 100 -s "from simpleanalyse import upgraded_erat_alh" "upgraded_erat_alh(100)"
# результат 100 loops, best of 5: 12.9 usec per loop

# Тут конечно не совсем корректный результат - не хватает поиска i-го простого в последнем случае, однако он не сильно
# замедлит Эратосфена и, мне кажется, при известном интервале поиска, Эратосфен быстрее.


# Описание тестов

def test_simple_alh(func):
    n = 14
    simple_list = [2, 3, 5, 7, 11, 13]
    assert func(n) == simple_list
    print('SIMPLE TEST DONE')

def test_erat_alh(func):
    n = 14
    erat_list = [2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0]
    assert func(n) == erat_list
    print('ERAT TEST DONE')

def test_find_simple(func):
    simple_list = [2, 3, 5, 7, 11, 13]
    for index, item in enumerate(simple_list):
        if item == func(index + 1):
            print(index + 1, ' - PASSED')
        else:
            print(index + 1, ' - WRONG - ', func(index + 1))

if __name__ == '__main__':
    # test_erat_alh(erat_alh_power)
    # test_erat_alh(upgraded_erat_alh)
    # test_simple_alh(simple_power)
    # test_find_simple(find_i_simple_num)

    run('upgraded_erat_alh(1000)')
    run('simple_power(1000)')
    run('find_i_simple_num(25)')
