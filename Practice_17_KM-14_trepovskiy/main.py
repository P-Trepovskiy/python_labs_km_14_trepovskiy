from exp_root.exponentiation import *
from factorial.factorial import *
from logarithm.logarithm import *


print('1. Факторіал')
print('2. Піднесення до квадрату')
print('3. Піднесення до кубу')
print('4. Логарифм')
print('5. Натуральний логарифм')
print('6. Десятковий логарифм')
try:
    choosed_func = int(input('Оберіть функцію: '))

    while choosed_func not in range(1, 7):
            print('Неправильне введення.')
            choosed_func = int(input('Оберіть функцію: '))
except ValueError:
    print('Неправильне введення.')

if choosed_func == 1:
    try:
        a = int(input('Введіть число: '))
        if a <= 0:
            print('Неправильне введення.')
            a = int(input('Введіть число: '))
            while a <= 0:
                print('Неправильне введення.')
                a = int(input('Введіть число: '))
        else:
            print(fact(a))
    except ValueError:
        print('Неправильне введення.')
elif choosed_func == 2:
    try:
        a = int(input('Введіть число: '))
        print(exp2(a))
    except ValueError:
        print('Неправильне введення.')
elif choosed_func == 3:
    try:
        a = int(input('Введіть число: '))
        print(exp3(a))
    except ValueError:
        print('Неправильне введення.')
elif choosed_func == 4:
    try:
        a = int(input('Введіть число: '))
        b = int(input('Введіть основу: '))
        while a < 0 or a == 1:
            print('Неправильне введення.')
            a = int(input('Введіть число: '))
            b = int(input('Введіть основу: '))
        print(log(a, b))
    except ValueError:
        print('Неправильне введення.')

elif choosed_func == 5:
    try:
        a = int(input('Введіть число: '))
        print(ln(a))
    except ValueError:
        print('Неправильне введення.')

elif choosed_func == 6:
    try:
        a = int(input('Введіть число: '))
        print(lg(a))
    except ValueError:
        print('Неправильне введення.')