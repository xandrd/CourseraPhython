def distance(x1, y1, x2, y2):
    s1 = x1 - x2
    s2 = y1 - y2
    r = (s1**2 + s2**2)**(1/2)
    return r

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

d1 = distance(x1, y1, x2, y2)
d2 = distance(x2, y2, x3, y3)
d3 = distance(x3, y3, x1, y1)

print(d1 + d2 + d3)
