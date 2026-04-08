arr = [-2,1,-3,4,-1,2,1,-5,4]

currsum = arr[0]
maxsum = arr[0]

for i in range(1, len(arr)):
    currsum = max(arr[i], currsum + arr[i])
    maxsum = max(maxsum, currsum)

print(maxsum)
