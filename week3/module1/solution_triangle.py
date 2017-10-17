a = float(input())
b = float(input())
c = float(input())

P = (a+b+c)/2  # полупериметр
S2 = P*(P-a)*(P-b)*(P-c)  # квадрат плозади по формуле полупериметров
S = S2 ** 0.5
print(S)
