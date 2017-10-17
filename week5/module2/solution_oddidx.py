arr = list(map(int, input().split()))

if len(arr) > 1:
    for idx in range(len(arr)//2):
        print(arr[idx*2+1], end=' ')
