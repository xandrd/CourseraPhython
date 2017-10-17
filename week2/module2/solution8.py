a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

# определим самую мальенькую сторону
# a >= b >= c
if c > b:
    (c, b) = (b, c)
if b > a:
    (a, b) = (b, a)
if c > b:
    (c, b) = (b, c)

# print(a, b, c)

s1 = (b <= d and c <= e)
s2 = (b <= e and c <= d)

if s1 or s2:
    print('YES')
else:
    print('NO')
