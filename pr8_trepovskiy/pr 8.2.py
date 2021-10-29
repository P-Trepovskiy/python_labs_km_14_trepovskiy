import math
import sys
try:
    a = float(input('Введіть число а: '))
    b = float(input('Введіть число b: '))
    c = float(input('Введіть число c: '))
except:
    print('Неправильне введення чисел.')
    sys.exit()
try:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        raise Exception('Discriminant error')
    x1 = (b * (-1) - math.sqrt(discriminant)) / a * 2
    x2 = (b * (-1) + math.sqrt(discriminant)) / a * 2
    print(f'Корені рівняння: {round(x1, 3)}, {round(x2, 3)}')
except ZeroDivisionError as e:
    print(e)
    print('a не може дорівнювати 0, так як при обчисленні коренів виконується ділення на 0.')
except Exception:
    print('Дискримінант менше 0, рівняння не має коренів.')
