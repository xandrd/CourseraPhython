arr = list(map(int, input().split()))
if len(arr) > 1:
    for idx in range((len(arr)+1)//2):
        print(arr[idx*2], end=' ')
else:
    print(arr[0])
