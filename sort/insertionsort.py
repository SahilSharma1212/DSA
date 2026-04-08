arr= [1,2,3,4,5,6,7,8,9]


for i in range(1,len(arr)):
    j = i
    while arr[j] > arr[j-1] and j >= 1:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j = j-1
print(arr)