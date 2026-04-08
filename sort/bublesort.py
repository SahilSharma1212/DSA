arr = [9,8,7,6,5,4,3,2,1]


for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j] < arr[i]:
            arr[j] , arr[i] = arr[i] , arr[j]

print(arr)