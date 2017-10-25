S, N = tuple(map(int, input().split()))
if N == 0:
    print(0)
else:
    A = []
    while len(A) < N:
        A.append(int(input()))
    A.sort()
    ss = 0
    res = 0
    idx = 0
    while idx < N and ss <= S:
        ss += A[idx]
        idx += 1
        if ss <= S:
            res += 1

    print(res)
