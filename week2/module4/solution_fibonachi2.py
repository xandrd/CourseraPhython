n = int(input())

if n == 0:
    r = 0
elif n == 1:
    r = 1

# F[0] =0, F[1] = 1, ..., F[n] = F[n-1] + F[n-2].

n1 = 0
n2 = 1
i = 1


if n > 1:
    while i < n:
        r = n1 + n2
        n1 = n2
        n2 = r
        i += 1

print(r)
