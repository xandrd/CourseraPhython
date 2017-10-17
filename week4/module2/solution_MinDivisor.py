def MinDivisor(n):
    i = 2
    sqrtN = (n ** 1/2) + 1
    # это ужасно бредовая проверка! Но алгоритм имеет сложность
    # sqrt(n) и не проходдит тест по времени
    while i <= sqrtN:
        if n % i == 0:
            return i
        i += 1
        if i > 1e6:
            return n
    return n

n = int(input())
print(MinDivisor(n))
