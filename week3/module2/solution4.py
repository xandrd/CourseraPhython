import math
p = float(input())
x = int(input())
y = int(input())
kk = int(input())

i = 1
while i <= kk:
    m = x*100 + y
    mp = math.floor(float((m + m*p/100)))/100

    k = mp - math.floor(mp)
    r = mp - k
    x = r
    y = round(k*100)
    i += 1
print(int(r), int(round(k*100)))
