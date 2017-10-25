fid = open('input.txt', 'r', encoding='utf8')
arr = []
for line in fid:
    surname, name,  n1, n2 = tuple(line.split())
    arr.append((surname, name, n1, n2))
fid.close()
arr.sort(key=lambda x: (x[0], x[1]))

fid = open('output.txt', 'w', encoding='utf8')
for line in arr:
    print(line[0], line[1], line[3], file=fid)
fid.close()
