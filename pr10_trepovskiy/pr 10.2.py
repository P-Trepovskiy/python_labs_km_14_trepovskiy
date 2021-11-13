import numpy as np


years = np.arange(1900, 2020+3, 1)


def find_high_precision_years():
    high_precision_years = []
    for i in years:
        if i % 400 == 0:
            high_precision_years.append(i)
        else:
            if i % 100 == 0:
                pass
            else:
                if i % 4 == 0:
                    high_precision_years.append(i)
    return high_precision_years


def days_in_month(month, year, func):
    if month % 2 != 0 or month == 8 or month == 12:
        return 31
    elif month != 2:
        return 30
    elif month == 2:
        if year in func:
            return 29
        else:
            return 28


month_num = input('Введіть місяць: ')
year_num = input('Введіть рік: ')
try:
    if int(month_num) < 0 or int(month_num) > 12:
        print('Неправильне введення місяця.')
    if len(list(year_num)) != 4 or int(year_num) < years[0]:
        print('Неправильне введення року.')
    else:
        print(f'Днів у цьому місяці: {days_in_month(int(month_num), int(year_num), find_high_precision_years())}')
except ValueError:
    print('Помилка!')
