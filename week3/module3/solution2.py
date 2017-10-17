s = input()
f = 'f'

p1 = s.find(f)
p2 = len(s) - 1 - s[::-1].find(f)

if p1 >= 0:
    if p2 != p1 and p2 >= 0:
        print(p1, p2)
    else:
        print(p1)
