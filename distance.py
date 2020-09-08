from math import radians, sin, cos, acos

print("Input coordinates of two points:")
slat = radians(float(input(" latitude 1: ")))
slon = radians(float(input(" longitude 1: ")))
elat = radians(float(input("latitude 2: ")))
elon = radians(float(input("longitude 2: ")))

dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
dist = dist * 1000
dist = int(dist)
print("The distance is: ", dist, " meters.")

# 10.726563, 106.710342
# 10.726724, 106.708470 popeyes
# 10.726529, 106.710106 artisen bakery
# 10.791083, 106.654190 cho tan binh
