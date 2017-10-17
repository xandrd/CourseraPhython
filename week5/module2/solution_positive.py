arr = list(map(int, input().split()))
p = 0
for idx in range((len(arr))):
    if arr[idx] > 0:
        p += 1
print(p)
