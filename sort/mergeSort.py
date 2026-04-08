
def merge(leftArr, rightArr):
    merged = []

    i = 0
    j = 0

    leftLen = len(leftArr)
    rightlen = len(rightArr)

    while i < leftLen and j < rightlen:
        if leftArr[i] < rightArr[j]:
            merged.append(leftArr[i])
            i = i+1
        else:
            merged.append(rightArr[j])
            j= j+1
    
    while i < leftLen:
        merged.append(leftArr[i])
        i = i+1
    
    while j < rightlen:
        merged.append(rightArr[j])
        j = j+1

    return merged

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2

    leftArr = merge_sort(arr[:mid])
    rightArr = merge_sort(arr[mid:])

    return merge(leftArr, rightArr)

# Example array
arr = [38, 27, 43, 3, 9, 82, 10]

# Call merge sort
sorted_arr = merge_sort(arr)

# Print sorted array
print(sorted_arr)