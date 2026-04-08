s = "ahbgdc"
t = "abc"
i = 0
for a in s:
    if i == len(t):
        print("IS A SUBSEQUENCE BRO")
        break

    if a == t[i]:
        i += 1

if i == len(t):
    print("IS A SUBSEQUENCE BRO")
else:
    print("NOT A SUBSEQUENCE")