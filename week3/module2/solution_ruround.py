import math

n = float(input())

if math.fabs(n % int(n) - 0.5) < 1e-21:
    print(math.ceil(n))
else:
    print(round(n))
