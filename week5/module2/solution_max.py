arr = list(map(int, input().split()))
i = 0
m = arr[i]
if len(arr) > 1:
    for idx in range(1, (len(arr))):
        if arr[idx] >= m:
            m = arr[idx]
            i = idx
print(m, i)
