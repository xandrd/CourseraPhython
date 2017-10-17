n = int(input())
x = float(input())
a = float(input())
# P(x)=a[n] xⁿ+a[n₋₁] xⁿ⁻¹+...+a[₁] x+a[₀]
# p(x)=a[n] xⁿ+a[n₋₁] xⁿ⁻¹+ +a[2] x2**2+a[1]x+a[0] = ...+x(a[2]x + a[1]) + a0

b = a

while n > 0:
    a = float(input())
    b = a + b*x
    n -= 1

print(b)
