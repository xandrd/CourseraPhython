k = int(input())

while N // 10 != 0:
    print(N % 10, end='')
    N = N // 10
print(N, end='')
