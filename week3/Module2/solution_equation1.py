from math import sqrt, fabs


a = float(input())
b = float(input())
c = float(input())

#  Дискриминант
d = b**2 - 4*a*c

if d >= 0:
    d = sqrt(d)
    x1 = (-b - d) / 2 / a
    x2 = (-b + d) / 2 / a
    if fabs(x1 - x2) < 1e-60:
        print(x1)
    else:
        print(x1, x2)
#  elif d == 0:
#    x1 = -b / 2 / a
#    print(x1)
