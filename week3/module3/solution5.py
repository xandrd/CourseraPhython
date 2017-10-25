s = input()
f = 'f'

p1 = s.find(f)
p2 = s.find(f, p1+1)

if p1 >= 0:
    if p2 >= 0 and p2 != p1:
        print(p2)
    else:
        print(-1)
else:
    print(-2)
