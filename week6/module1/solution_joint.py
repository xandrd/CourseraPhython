def merge(A, B):
    res = []
    lenA = len(A)
    lenB = len(B)
    idxA = 0
    idxB = 0
    idx = 0
    v = min(A[0], B[0])

    while idx < lenA + lenB:

        if idxA < lenA and idxB < lenB:
            if A[idxA] < B[idxB]:
                v = A[idxA]
                idxA += 1
            else:
                v = B[idxB]
                idxB += 1
        elif idxA < lenA:
            v = A[idxA]
            idxA += 1
        else:
            v = B[idxB]
            idxB += 1

        idx += 1
        res.append(v)

    return res


A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*merge(A, B))
