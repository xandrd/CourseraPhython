arr = list(map(int, input().split()))
m = arr[0]
for idx in range(len(arr)):
    if (m < 0) and (arr[idx] > 0):
        m = arr[idx]

    if (arr[idx] > 0) and (arr[idx] < m):
        m = arr[idx]
print(m)
