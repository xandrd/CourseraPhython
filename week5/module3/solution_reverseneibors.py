arr = list(map(int, input().split()))
n = 2*(len(arr) // 2)

for k in range(0, n, 2):
    i = k
    j = k+1
    arr[i], arr[j] = arr[j], arr[i]

print(*arr)
