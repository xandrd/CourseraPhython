def ReduceFraction(n, m):
    # сначала выберем максимальное число
    if n >= m:
        nod = n
    else:
        nod = m
    d = 2

    while d <= nod:
        if n % d == 0 and m % d == 0:
            n, m = ReduceFraction(n // d, m // d)
        d += 1
        # Опять это тупое условие
        if d > 1e6:
            return n, m
    return n, m


n = int(input())
m = int(input())
q, p = ReduceFraction(n, m)
print(q, p)
