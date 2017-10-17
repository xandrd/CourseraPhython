k = int(input())

i = 1  # цикл
c = 0  # счетчик полиндромов

while i <= k:
    N = i
    S = ''

    # определяем обратное число
    while N // 10 != 0:
        S += str(N % 10)
        N = N // 10
    S += str(N)
    P = int(S)
    if P == i:
        c += 1
        # print(S, i)
    i += 1

print(c)
