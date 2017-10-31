n = int(input())
line = input()
Q = set(range(1, n+1))
while line != 'HELP':
    if line == 'YES':
        Q = T
    elif line == 'NO':
        Q = Q - T
    else:
        T = set(map(int, line.split()))
    line = input()

print(*sorted(list(Q)))
