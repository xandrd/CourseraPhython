x = float(input())
y = float(input())

d = 1

if y <= x:
    print(1)
else:
    while x < y:
        d += 1
        x *= 1.1
    print(d)
