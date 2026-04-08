arr = [1,1,0,0,1,1,1,1,0,1]

maxcount = 0
currcount = 0
for i in range(len(arr)):
    if arr[i] == 1:
        currcount += 1
    else:
        currcount = 0
    maxcount = max(currcount, maxcount)


print(maxcount)