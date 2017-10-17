a = int(input())
b = int(input())
c = int(input())
d = int(input())

if c * b == a * d:
    print("NO")
elif a == 0 and b == 0:
    print("INF")
else:
    print(-b//a)
