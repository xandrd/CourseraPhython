arr = list(map(int, input().split()))

mval = arr[0]
Mval = arr[0]
mi = 0
Mi = 0

for k in range(len(arr)):
    if arr[k] > Mval:
        Mval = arr[k]
        Mi = k
    if arr[k] < mval:
        mval = arr[k]
        mi = k

arr[mi], arr[Mi] = arr[Mi], arr[mi]

print(*arr)
