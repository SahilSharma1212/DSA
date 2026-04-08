s = "SahilSarmae"

s2 = "Sahi"

if s2 in s:
    print(True)

    
s3 = sorted(s)
print(s3)


st = {"a", "1", "A"}
print(sorted(st))

st2 = {"1", "a", "A"}
ans = set(sorted(st))
ans2 = set(sorted(st2))
print(ans, ans2)