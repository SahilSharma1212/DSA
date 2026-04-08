mp = {
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
}

s = "46"

n = len(s)
ans = []
def letterCombination(i, curr):
    if i == n:
        ans.append(curr)
        return
    
    for el in mp[s[i]]:
        letterCombination(i+1, curr + el)


letterCombination(0, "")
print(ans)