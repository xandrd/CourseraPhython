n = int(input())
myDict = dict()
for i in range(n):
    (word, syn) = input().split()
    myDict[syn] = word
    myDict[word] = syn

print(myDict[input()])
