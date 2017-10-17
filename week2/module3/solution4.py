N = int(input())

k = 0
i = 1
while i <= N:
    if i == N:
        print('YES')
        flag = False
        break
    i = i * 2

if flag:
    print('NO')
