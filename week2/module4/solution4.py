n = int(input())
i = 0
p = n

while n != 0:
    if n > p:
        i += 1
    p = n
    n = int(input())


print(i)
