def power(a, n):
    # aⁿ = (a²)ⁿ/² при четном n,
    # aⁿ=a⋅aⁿ⁻¹ при нечетном n.

    # выход из рекурсии
    if n <= 0:
        return 1

    if n % 2 == 0:
        return power(a * a, n // 2)
    else:
        return a*power(a, n - 1)

a = float(input())
n = int(input())

print(power(a, n))
