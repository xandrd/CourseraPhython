def rever():
    n = int(input())
    if n != 0:
        rever()
    print(n)


rever()
