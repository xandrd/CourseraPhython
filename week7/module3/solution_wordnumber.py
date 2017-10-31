fid = open('input.txt')
lines = fid.readlines()
fid.close()

words = []
for line in lines:
    words.extend(line.split())

wordsDict = dict()
for word in words:
    wordsDict[word] = wordsDict.get(word, -1) + 1
    print(wordsDict[word], end=' ')
