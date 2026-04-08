def combinationSum(arr, index, ans, curr, tar, total):
    if total == tar:
        ans.append(curr.copy())
        return
    elif total > tar:
        return

    if index == len(arr):
        return

    # pick element (can reuse same index)
    curr.append(arr[index])
    combinationSum(arr, index, ans, curr, tar, total + arr[index])
    
    # backtrack
    curr.pop()
    
    # skip element
    combinationSum(arr, index+1, ans, curr, tar, total)