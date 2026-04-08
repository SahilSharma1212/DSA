n = 19191
s = str(19191)
size = len(s)
ans = True
for i in range(size):
    if s[i] != s[size - i -1]:
        ans = False
    i += 1

print (ans)