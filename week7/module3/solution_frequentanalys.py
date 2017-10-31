import sys
words = ' '.join(sys.stdin.readlines()).split()

myDict = {}
for word in words:
    myDict[word] = myDict.get(word, 0) + 1

myWords = []
for word in sorted(myDict):
    myWords.append((myDict[word], word))

for word in sorted(myWords, reverse=True, key=lambda x: x[0]):
    print(word[1])
