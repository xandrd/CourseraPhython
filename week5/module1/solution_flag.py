n = int(input())
f = ('+___ ', '|__\ ', '|    ')

for i in range(1, n+1):
    print(f[0], end=' ')

print('')


for i in range(1, n+1):
    print('|' + str(i) + ' / ', end=' ')

print('')

for i in range(1, n+1):
    print(f[1], end=' ')

print('')

for i in range(1, n+1):
    print(f[2], end=' ')

print('')
