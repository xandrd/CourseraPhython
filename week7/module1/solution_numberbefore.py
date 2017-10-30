nlist = list(map(int, input().split()))
s = set()

for n in nlist:
    if n in s:
        print('YES')
    else:
        print('NO')
        s.add(n)
