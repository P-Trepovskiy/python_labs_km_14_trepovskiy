def fact(n):
    if n == 1:
        return n
    else:
        fac = n * fact(n-1)
    return fac
