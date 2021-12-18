import math


def newton(n):
    k = 0
    while k <= n:
        yield math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
        k += 1

x = int(input('Введіть число: '))
if x <= 0:
    print('Введене неправильне число.')
    x = int(input('Введіть число: '))
    while x <= 0:
        print('Введене неправильне число.')
        x = int(input('Введіть число: '))
x = (i for i in range(x+1))
for i in x:
    newt = newton(i)
    for i in range(i + 1):
         print(int(next(newt)), end=' ')
    print('')
