from math import fabs
a = float(input())
b = float(input())
c = float(input())

d = float(input())
e = float(input())
f = float(input())

#  ax + by = e
#  cx + dy = f
#  x = (e - by)/a
#  c*(e - by)/a + dy = f
#  c*e/a - c*by/a + dy = f
#  -c*by/a + dy = f - c*e/a
#  y(-c*b/a + d) = f - c*e/a
#  y = (f - ce/a) / (-c*b/a + d)

if int(a) != 0 and fabs(d * a - c * b) > 1e-10:
    y = (f * a - c * e) / (d * a - c * b)
    x = (e - b * y) / a
else:
    y = (c * e - a * f) / (b * c - d * a)
    x = (f - d * y) / c

print(x, y)
