# L ----> R (only)

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# SUBSEQUENCES ARE :
# [1, 3, 4, 8]


# EXAMPLE = [1, 2, 3] => [], [1], [2], [3], [1,2], [1,3], [2, 3], [1, 2, 3]

def generateSubSequence(arr, idx, currArr, currSum, tar):
    # if final reached
    if currSum == tar:
        return True
    if idx == len(arr):
        return
    # not reached
    
    currArr.append(arr[idx])
    currSum += arr[idx]
    selectedResponse = generateSubSequence(arr, idx+1, currArr, currSum, tar)
    
    currArr.pop()
    currSum -= arr[idx]
    notSelectedResponse = generateSubSequence(arr, idx+1, currArr, currSum, tar)

    return selectedResponse or notSelectedResponse




arr = [1,2,3,4]
tar = 5


print(generateSubSequence(arr, 0, [], 0, tar))