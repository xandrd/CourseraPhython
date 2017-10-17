n = float(input())
i = 1
r = 1
#  1+(1 / 2²)+(1 / 3²)+...+(1 / n²).
while i < n:
    i += 1
    r += 1 / (i*i)

print(r)
