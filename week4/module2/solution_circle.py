def IsPointInCircle(x, y, xc, yc, r):
    s1 = x - xc
    s2 = y - yc
    R = (s1 ** 2 + s2 ** 2) ** (1 / 2)
    return R <= r

x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())

if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
