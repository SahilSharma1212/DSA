s = "tree"
mp = {}

for i in s:
    if i not in mp:
        mp[i] = 1
    else:
        mp[i] += 1

countmap = {}
print(mp)
for key in mp:
    
    if mp[key] not in countmap:
        countmap[mp[key]] = [key]
    else:
        countmap[mp[key]].append(key)

print(sorted(countmap))