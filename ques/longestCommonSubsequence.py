arr = [1, 99, 101, 98, 2, 5, 3, 99, 100]

s = set()

s.update(arr)
maxcount = 1
for i in s:
    currcount = 1
    curnum = i
    if i-1 not in s:
        
        while curnum+1 in s:
            currcount += 1
            curnum += 1
    maxcount = max(currcount, maxcount)

print(maxcount)