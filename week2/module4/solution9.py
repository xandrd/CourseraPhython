A = int(input())
B = int(input())

while B < A:
    if A % 2 == 0 and A // 2 >= B:
        A //= 2
        print(':2')
    else:
        A -= 1
        print('-1')
