n = 4
k = 2
ans = []

def combinationSum3(i, c, curr):
    # correct base case
    if c == k:
        ans.append(curr.copy())
        return

    if i > n:
        return

    # not including
    combinationSum3(i + 1, c, curr)

    # including
    curr.append(i)
    combinationSum3(i + 1, c + 1, curr)
    curr.pop()

combinationSum3(1, 0, [])
print(ans)