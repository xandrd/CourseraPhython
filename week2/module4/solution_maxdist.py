n0 = int(input())
n1 = int(input())
n2 = int(input())

# Начальные данные
Dist = 0
maxDist = 0
resDist = 0

while n2 != 0:
    #  print(n0, n1, n2, Dist, maxDist, resDist)

    if n1 > n2 and n1 > n0:
        # это новый локальный максимум
        maxDist = Dist
        if maxDist < resDist or resDist == 0:
            resDist = maxDist
        # print(n0, n1, n2, Dist, resDist)
        Dist = 0

    Dist += 1
    n0 = n1
    n1 = n2
    n2 = int(input())

print(resDist)
