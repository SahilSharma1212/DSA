n = 3

def genAllBinStrings(n, ans, curr, i):
    if i == n:
        ans.append(curr.copy())
        return

    curr.append(0)
    genAllBinStrings(n, ans, curr, i+1)

    curr.pop()
    curr.append(1)
    genAllBinStrings(n, ans, curr, i+1)
    curr.pop()

ans = []

genAllBinStrings(n, ans, [], 0)
print(ans)