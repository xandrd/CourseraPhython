n = int(input())

va = n == 1 or (n > 20 and ((n-1) % 10 == 0))
vy0 = n == 2 or n == 3 or n == 4
vy2 = ((n-2) % 10 == 0)
vy3 = ((n-3) % 10 == 0)
vy4 = ((n-4) % 10 == 0)
vy = vy0 or (n > 20 and (vy2 or vy3 or vy4))

if va:
    print(n, 'korova')
else:
    if vy:
        print(n, "korovy")
    else:
        print(n, "korov")
