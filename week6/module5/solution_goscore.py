from gc import enable

fid = open('input.txt', 'r', encoding='utf8')
arr = []
min_scr = 40
max_spot = int(fid.readline())
for line in fid:
    # Вот жеж гребанный входные данные!
    # surname, name,  n1, n2, n3 = tuple(line.split())
    row = line.split()
    (s1, s2, s3) = map(int, (row[-3], row[-2], row[-1]))
    if (s1 >= min_scr) and (s2 >= min_scr) and (s3 >= min_scr):
        arr.append(s1 + s2 + s3)
fid.close()

got_spot = 0
score_spot = 0
current_scr = -1
if len(arr) != max_spot:
    arr.sort(reverse=True)
    max_scr = max(arr)
    previous_scr = max(arr)
    current_scr = max(arr)

    for i in range(len(arr)):
        if arr[i] == current_scr and got_spot <= max_spot:
            got_spot += 1
        elif arr[i] < current_scr and got_spot <= max_spot:
            previous_scr = current_scr
            current_scr = arr[i]
            got_spot += 1

        if got_spot > max_spot:
            current_scr = previous_scr

    if (current_scr == max_scr) and (got_spot > max_spot):
        current_scr = 1
else:
    current_scr = 0

print(*arr)
print(current_scr, max_spot, got_spot)
#fid = open('output.txt', 'w', encoding='utf8')
#print(current_scr, file=fid)
#fid.close()
