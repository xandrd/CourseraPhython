n1 = int(input())
n2 = int(input())
m1 = n1
m2 = n2

while n2 != 0:
    if n2 >= m1:
        m2 = m1
        m1 = n2
    elif n2 >= m2:
        m2 = n2

    n2 = int(input())

print(m2)
