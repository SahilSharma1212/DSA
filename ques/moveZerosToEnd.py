a = [1,0,2,4,3,0,0,3,5]

zeroIdx = 0

for i in range(len(a)):
    if a[i] != 0:
        a[i], a[zeroIdx] = a[zeroIdx], a[i]
        zeroIdx += 1
print(a) 