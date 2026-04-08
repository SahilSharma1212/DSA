# L ----> R (only)

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# SUBSEQUENCES ARE :
# [1, 3, 4, 8]


# EXAMPLE = [1, 2, 3] => [], [1], [2], [3], [1,2], [1,3], [2, 3], [1, 2, 3]

def generateSubSequence(arr, idx, currArr, ans, currSum, tar):
    # if final reached
    if currSum == tar:
        ans.append(currArr.copy())
        return
    if idx == len(arr):
        return
    # not reached
    
    currArr.append(arr[idx])
    currSum += arr[idx]
    generateSubSequence(arr, idx+1, currArr, ans, currSum, tar)
    
    currArr.pop()
    currSum -= arr[idx]
    generateSubSequence(arr, idx+1, currArr, ans, currSum, tar)




ans = []
arr = [1,2,3,4]
tar = 5
generateSubSequence(arr, 0, [], ans, 0, tar)

print(ans)