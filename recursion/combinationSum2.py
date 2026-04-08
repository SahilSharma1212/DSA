arr = [1,2,1,2,1]
tar = 4
ans = []
arr.sort()

def backtrack(start, curr, total):
    if total == tar:
        ans.append(curr.copy())
        return

    for i in range(start, len(arr)):
        if i > start and arr[i] == arr[i-1]:
            continue

        if arr[i] + total > tar:
            break

        curr.append(arr[i])
        backtrack(i+1, curr, total + arr[i])
        curr.pop()


backtrack(0, [], 0)
print(ans)