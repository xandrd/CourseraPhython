n = int(input())
L = []
for i in range(n):
    name, score = tuple(input().split())
    L.append((name, -1*int(score)))

L.sort(key=lambda x: x[1])

for l in L:
    print(l[0])
