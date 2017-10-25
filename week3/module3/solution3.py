s = input()
f = 'h'

p1 = s.find(f)
p2 = len(s) - 1 - s[::-1].find(f)
print(s[:p1] + s[p2+1:])
