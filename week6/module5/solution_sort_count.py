def CountSort(A):
    numbers = [0] * 101

    for n in A:
        numbers[n] += 1
    B = []

    for i in range(len(numbers)):
        for j in range(numbers[i]):
            B.append(i)
    return B


A = list(map(int, input().split()))
B = CountSort(A)
print(*B)
