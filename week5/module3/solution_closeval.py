a = int(input())
arr = list(map(int, input().split()))
x = int(input())

val = arr[0]
delta = abs(x - arr[0])

for i in range(len(arr)):
    if abs(x - arr[i]) < delta:
        delta = abs(x - arr[i])
        val = arr[i]

print(val)
