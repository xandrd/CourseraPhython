n = int(input())
m = int(input())
k = int(input())

toBig = k > n*m
nSide = k % n == 0
mSide = k % m == 0

if (nSide or mSide) and not toBig:
    print("YES")
else:
    print("NO")
