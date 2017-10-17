arr = list(map(int, input().split()))
for idx in range((len(arr))):
    if arr[idx] % 2 == 0:
        print(arr[idx], end=' ')
