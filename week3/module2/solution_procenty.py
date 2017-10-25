import math
p = float(input())
x = int(input())
y = int(input())

v = 100*x + y
v = v*p/100 + v

print(int(v // 100), int(v % 100))
