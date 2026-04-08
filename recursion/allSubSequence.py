# L ----> R (only)

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# SUBSEQUENCES ARE :
# [1, 3, 4, 8]


# EXAMPLE = [1, 2, 3] => [], [1], [2], [3], [1,2], [1,3], [2, 3], [1, 2, 3]

def generateSubSequence(arr, idx, curr, ans):
    # if final reached
    if idx == len(arr):
        ans.append(curr.copy())
        return
    # not reached
    
    curr.append(arr[idx])
    generateSubSequence(arr, idx+1, curr, ans)
    
    curr.pop()
    generateSubSequence(arr, idx+1, curr, ans)




ans = []
arr = [1,2,3]
generateSubSequence(arr, 0, [], ans)

print(ans)