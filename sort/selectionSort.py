arr = [1,2,3,4,5,6,7,9]


for i in range(len(arr)):
    currmax = i
    for j in range(i, len(arr)):
        if arr[j] > arr[currmax]:
            currmax = j
    arr[i], arr[currmax] = arr[currmax], arr[i]

print(arr)