def rrange(begin:int, end:int, step=1):
    if begin < end:
        if step < 0:
            return []
    elif begin > end:
        if step > 0:
            return []
    if step == 0:
        return []
    else:
        lst = []
        for i in range(begin, end, step):
            lst.append(i)
        return lst


x = rrange(1, 10)
y = rrange(10, 1, -1)
z = rrange(10, 1, 1)
print(x, y, z)
assert x == list(range(1, 10)), 'Failed test for simple range'
assert y == list(range(10, 1, -1)), 'Failed test for reverse range'
assert z == list(range(10, 1, 1)), 'Failed test for empty range'
print('All tests good!')