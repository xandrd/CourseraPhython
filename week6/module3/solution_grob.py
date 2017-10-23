nCity = int(input())
aCity = list(map(int, input().split()))

nBomb = int(input())
aBomb = list(map(int, input().split()))

# список селений
lCity = []
for i in range(nCity):
    lCity.append((i+1, aCity[i]))

lBomb = []
for i in range(nBomb):
    lBomb.append((i+1, aBomb[i]))

lCity.sort(key=lambda x: x[1])
lBomb.sort(key=lambda x: x[1])

# print(lCity)
# print(lBomb)

res = []

foundBomb = 0
currentBomb = 0
maxDist = max(lCity[-1][1], lBomb[-1][1])

for i in range(nCity):
    j = currentBomb
    dist = abs(lCity[i][1] - lBomb[j][1])
    currentRecord = (lCity[i][0], lBomb[j][0])
    while j < nBomb and abs(lCity[i][1] - lBomb[j+1][1]) < dist:
        dist = abs(lCity[i][1] - lBomb[j+1][1])
        currentRecord = (lCity[i][0], lBomb[j+1][0])
        j += 1
        currentBomb = j

    res.append(currentRecord)

res.sort(key=lambda x: x[0])

# print(len(res))
# print(res)
for i in range(nCity):
    print(res[i][1], end=' ')

