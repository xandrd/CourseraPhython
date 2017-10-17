roomX = int(input())
roomY = int(input())
roomZ = int(input())

noutX = int(input())
noutY = int(input())
noutZ = int(input())

size1 = (roomX // noutX) * (roomY // noutY) * (roomZ // noutZ)
size2 = (roomX // noutX) * (roomY // noutZ) * (roomZ // noutY)
size3 = (roomX // noutY) * (roomY // noutX) * (roomZ // noutZ)
size4 = (roomX // noutY) * (roomY // noutZ) * (roomZ // noutX)
size5 = (roomX // noutZ) * (roomY // noutX) * (roomZ // noutY)
size6 = (roomX // noutZ) * (roomY // noutY) * (roomZ // noutX)

sizeMax = size1
if size2 > sizeMax:
    sizeMax = size2
if size3 > sizeMax:
    sizeMax = size3
if size4 > sizeMax:
    sizeMax = size4
if size5 > sizeMax:
    sizeMax = size5
if size6 > sizeMax:
    sizeMax = size6

print(sizeMax)
