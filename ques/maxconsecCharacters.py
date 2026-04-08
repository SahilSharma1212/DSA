s = "abbcccddddeeeeedcba"

currcnt = 1
maxcnt = 1

for i in range(len(s)):
    if s[i] == s[i-1]:
        currcnt += 1
    else:
        currcnt = 1
    
    maxcnt = max(maxcnt, currcnt)

print(maxcnt)