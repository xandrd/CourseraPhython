fid = open('input.txt', 'r')
#  формируем множество
s = set()

for line in fid:
    l = set(line.split())
    s = s | l
fid.close()

print(len(s))
