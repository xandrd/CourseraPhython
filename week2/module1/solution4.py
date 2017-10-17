Y = int(input())

crat4 = Y % 4 == 0
crat100 = Y % 100 != 0
crat400 = Y % 400 == 0

vis = (crat4 and crat100) or crat400

if vis:
    print("YES")
else:
    print("NO")
