def power(a, n):
    if n != 0:
        return a * power(a, n-1)
    return 1

a = float(input())
n = int(input())

print(power(a, n))
