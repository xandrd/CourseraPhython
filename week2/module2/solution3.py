c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

moveUp = r2 > r1
sameLine = (c1+r1) % 2 == (c2+r2) % 2

if moveUp and sameLine:
    print('YES')
else:
    print('NO')
