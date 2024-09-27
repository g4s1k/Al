# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

# Если честно, решение через классы мне тут кажется наиболее логичным.


from collections import namedtuple, defaultdict, OrderedDict
from statistics import mean           # можно было бы написать свою функцию)


PARAMS = 'Enterpise_name, First_quarter_profit, Second_quarter_profit, Third_quarter_profit, Fourth_quarter_profit'
Enterpise = namedtuple('Enterpise', PARAMS)

print('Введите данные о предприятиях.')
print(f'Формат ввода: {PARAMS}')
print('После ввода данных о предприятиях введите команду END')

num = 1
base = defaultdict(int)

while True:
    income = input(f'Предприятие №{num}: ')
    num += 1

    if income.lower() == 'end':
        break

    income_list = income.split(' ')

    for index in range(1, 5):
        income_list[index] = int(income_list[index])

    base[Enterpise(*income_list)] = mean(income_list[1:5])

average_annual_profit = mean(base.values())
base['AAP'] = average_annual_profit
ordered_base = OrderedDict(sorted(base.items(), key = lambda x: x[1], reverse = True))

buf = 'Winners list:'
for key in ordered_base:
    if key == 'AAP':
        print(buf)
        buf = 'Losers list:'
    else:
        buf = ' '.join((buf, key.Enterpise_name))

print(buf)
