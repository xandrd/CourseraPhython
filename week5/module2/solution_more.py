arr = list(map(int, input().split()))

if len(arr) > 1:
    for idx in range(1, (len(arr))):
        if arr[idx] > arr[idx-1]:
            print(arr[idx], end=' ')
