arr = [1,2,3]
ans = []

n = len(arr)

def permute(currIndex, arr):
    if currIndex == n:
        ans.append(arr.copy())
        return
    # swapping part
    for i in range(currIndex, n):
        # swap
        arr[currIndex], arr[i] = arr[i], arr[currIndex]
        permute(currIndex+1, arr)
        # backtrack
        arr[currIndex], arr[i] = arr[i], arr[currIndex]


permute(0, n, arr)
print(ans)