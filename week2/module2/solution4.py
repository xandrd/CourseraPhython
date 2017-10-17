a = int(input())
b = int(input())
c = int(input())

# определим гипотинузу
if (a >= b) and (a >= c):
    g = a
    k1 = b
    k2 = c
elif (b >= a) and (b >= c):
    g = b
    k1 = a
    k2 = c
elif (c >= a) and (c >= b):
    g = c
    k1 = a
    k2 = b

if k1**2 + k2**2 == g**2:
    print('rectangular')
elif g**2-k1**2-k2**2-2*k1*k2 > 0:
    print('impossible')
elif k1**2+k2**2-g**2 > 0: # cos > 0 - острый
    print('acute')
else:
    print('obtuse')
