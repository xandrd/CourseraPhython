def distance(x1, y1, x2, y2):
    s1 = x1 - x2
    s2 = y1 - y2
    r = (s1**2 + s2**2)**(1/2)
    return r

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(distance(x1, y1, x2, y2))
