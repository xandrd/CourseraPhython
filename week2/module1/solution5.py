c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

mvSide = (c1+1 == c2 or c1-1 == c2) and (r1+1 == r2 or r1-1 == r2 or r1 == r2)
mvVert = (c1 == c2) and (r1+1 == r2 or r1-1 == r2)


if mvSide or mvVert:
    print("YES")
else:
    print("NO")
