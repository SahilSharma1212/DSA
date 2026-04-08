s = "egg"
t = "add"

mp1 = {}
mp2 = {}

isIso = True

if len(s) != len(t):
    isIso = False

for i in range(len(s)):
    if s[i] in mp1:
        if mp1[s[i]] != t[i]:
            isIso = False
            break
    else:
        mp1[s[i]] = t[i]

    if t[i] in mp2:
        if mp2[t[i]] != s[i]:
            isIso = False
            break
    else:
        mp2[t[i]] = s[i]

print(isIso)