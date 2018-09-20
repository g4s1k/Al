# Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N. Например, состоящая только из маленьких
# латинских букв. Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из
# модуля hashlib.


import hashlib


def subs_count(s):

    subs = set()

    for i in range(len(s) + 1):

        for j in range(i + 1, len(s) + 1):

            sub_s = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()

            subs.add(sub_s)

    return len(subs)


s = input('Введите строку: ')

print(f'В строке "{s}" {subs_count(s)} подстрок')