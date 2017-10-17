n = int(input())
m = n
i = 0

while n != 0:
    if n > m:
        m = n
        i = 1
    elif n == m:
        i += 1
    n = int(input())

print(i)
