a = [1,0,3,4]

xorsum = 0
arrxor = 0

for i in range(len(a) + 1):
    xorsum ^= i

for i in range(len(a)):
    arrxor ^= a[i]

print(xorsum ^ arrxor)