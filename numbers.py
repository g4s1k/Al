# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
#
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque


first, second = input('Введите два числа в шестнадцатеричной системе счисления через пробел: ').split(' ')

num_1 = list(first)
num_2 = list(second)
sum_result = deque()
mult_result = deque()

while num_1 or num_2:
    item_1 = 0
    item_2 = 0
    if num_1:
        item_1 = int(num_1.pop(), 16)

    if num_2:
        item_2 = int(num_2.pop(), 16)

    local_result = str(hex(item_1 + item_2))
    local_result = local_result.replace('0x', '')
    sum_result.appendleft(*list(local_result))
    local_result = str(hex(item_1 * item_2))
    local_result = local_result.replace('0x', '')
    mult_result.appendleft(*list(local_result))

print(f'Сумма: {sum_result}\nПроизведение: {mult_result}')
