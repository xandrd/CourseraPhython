n1 = int(input())
n2 = int(input())
c = 1
cm = 1

while n2 != 0:
    if n1 == n2:
        c += 1
    else:
        if c >= cm:
            cm = c
        c = 1

    n1 = n2
    n2 = int(input())

if c >= cm:
    cm = c

print(cm)
