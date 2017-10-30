fid = open('input.txt', 'r')
u1 = set(map(int, fid.readline().split()))
u2 = set(map(int, fid.readline().split()))
fid.close()
fid = open('output.txt', 'w')
print(*sorted(u1 & u2), file=fid)
fid.close
