def min4(a, b, c, d):
    r1 = min(a, b)
    r2 = min(c, d)
    return min(r1, r2)

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min4(a, b, c, d))
