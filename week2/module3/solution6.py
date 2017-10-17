x = float(input())
y = float(input())

if x != 0:
    day = 1
    if x == y:
        day -= 1

    while x <= y:
        x = x + 0.1*x
        # print(x)
        day += 1

    print(day)
else:
    print(0)
