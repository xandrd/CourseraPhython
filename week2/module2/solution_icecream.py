k = int(input())

m = k
check = True

while m > 0:
    if (m % 5) == 0:
        print('YES')
        exit(0)
    m -= 3

m = k
while m > 0:
    if (m % 3) == 0:
        print('YES')
        exit(0)
    m -= 5

print('NO')
