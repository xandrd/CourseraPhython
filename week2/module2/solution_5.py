a = int(input())
b = int(input())
c = int(input())

# проверка на четность
tA = a % 2 == 0
tB = b % 2 == 0
tC = c % 2 == 0

allt = tA and tB and tC
somet = tA or tB or tC

if (somet and not allt):
    print("YES")
else:
    print("NO")
