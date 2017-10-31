npuple = int(input())
A = set()
for i in range(npuple):
    nlang = int(input())
    T = set()
    for j in range(nlang):
        lang = input()
        T.add(lang)
    if i == 0:
        N = T
        A = T
    else:
        A = A | T
        N = N & T


print(len(N))
print(*N, sep='\n')
print(len(A))
print(*A, sep='\n')
