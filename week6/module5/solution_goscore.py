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
score_cnt = []
if len(arr) > max_spot:
    arr.sort(reverse=True)
    max_scr = max(arr)
    previous_scr = max(arr)
    current_scr = max(arr)

    idx = -1
    for a in arr:
        if len(score_cnt) > 0 and score_cnt[idx][0] == a:
            score_cnt[idx][1] += 1
        else:
            score_cnt.append([a, 1])
            idx += 1

    for a in score_cnt:
        if got_spot+a[1] <= max_spot:
            got_spot += a[1]
            current_scr = a[0]
        else:
            break

    if got_spot == 0:
        current_scr = 1


else:
    current_scr = 0

# print(score_cnt)
# print(current_scr, max_spot, got_spot)
fid = open('output.txt', 'w', encoding='utf8')
print(current_scr, file=fid)
fid.close()
