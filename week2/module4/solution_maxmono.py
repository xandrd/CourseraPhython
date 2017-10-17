n1 = int(input())
n2 = int(input())

# Начальные данные

monoMore = 0
monoLess = 0
maxMonoMore = 1
maxMonoLess = 1

if n1 > n2:
    monoMore += 1
    maxMonoMore += 1

if n1 < n2:
    monoLess += 1
    maxMonoLess += 1

while n2 != 0:
    # проверка More
    if n1 > n2:
        monoMore += 1
    elif monoMore >= maxMonoMore:
        maxMonoMore = monoMore
        monoMore = 0

    # проверка Less
    if n1 < n2:
        monoLess += 1
    elif monoLess >= maxMonoLess:
        maxMonoLess = monoLess
        monoLess = 0

    n1 = n2
    n2 = int(input())

# Если переключения поледовательности  не просиходило,
# 3запонить последнее значение
if monoMore >= maxMonoMore:
    maxMonoMore = monoMore

if monoLess >= maxMonoLess:
    maxMonoLess = monoLess

maxMono = maxMonoMore
if maxMonoLess > maxMono:
    maxMono = maxMonoLess

print(maxMono)
