fid = open('input.txt', 'r', encoding='utf8')
candidates = fid.readlines()
fid.close()

totalVotes = float(len(candidates))
election = dict()
for candidate in candidates:
    c = candidate.strip('\n')
    election[c] = election.get(c, 0) + 1

results = []
for who in election:
    results.append((float(election[who])/totalVotes, who))

results.sort(reverse=True)

fid = open('output.txt', 'w', encoding='utf8')
print(results[0][1], file=fid)
if results[0][0] <= 0.5:
    print(results[1][1], file=fid)
