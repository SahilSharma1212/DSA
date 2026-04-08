arr = [1,2,2,2,2,3,4,4,56,7,8,8,8,9,9,0]

mp = {}

arr2 = []

for i in arr:
    if i not in mp:
        mp[i] = 1
        arr2.append(i)
    else:
        mp[i] += 1

for el in mp:
    while mp[el] > 1:
        arr2.append(el)
        mp[el] -= 1

print(arr2)