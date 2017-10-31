import sys
words = ' '.join(sys.stdin.readlines()).split()
myDict = {}
for word in words:
    myDict[word] = myDict.get(word, 0) + 1

(w, m) = ('', 0)
for word in sorted(myDict):
    if myDict[word] > m:
        m = myDict[word]
        w = word

print(w)
