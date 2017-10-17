def summa(a):
    if a != 0:
        a += summa(int(input()))
    return a

a = int(input())
print(summa(a))
