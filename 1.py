# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9


RANGE_START = 2
RANGE_END = 99
DIV_START = 2
DIV_END = 9

ans = [0 for _ in range(DIV_END - DIV_START + 1)]
buf = ''

for num in range(RANGE_START, RANGE_END + 1):
    for div in range(DIV_START, DIV_END + 1):
        if num % div == 0:
            ans[div - DIV_START] += 1

for index in range(DIV_END - DIV_START + 1):
    buf = ' '.join((buf, str(DIV_START + index), '-', str(ans[index]), '\n'))

print(buf)
