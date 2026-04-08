stck = "(()())(())"

count = 0
ans = ""
for i in stck:
    
    if i == "(":
        count += 1
        if count > 1:
            ans += i
    if i == ")":
        count -= 1
        if count > 0:
            ans += i

print(ans)