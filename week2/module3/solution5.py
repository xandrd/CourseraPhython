N = int(input())

# 2**k >= N

k = 0
t = 1
while t < N:
    t *= 2
    k += 1

print(k)
