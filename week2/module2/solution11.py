k = int(input())

# случай 1
c5 = k % 5

# случай 2
c3 = k % 3

if k != 0 and (c5 % 3 == 0 or c3 % 5 == 0):
    print('YES')
else:
    print('NO')
