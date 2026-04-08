arr = [1,2,3,4,5,6,7,8,9,10]

# leftarr = arr[-3:]
# rightArr = arr[:-3]

# arr.reverse()

# arr = leftarr + rightArr

arr.reverse()

arr = arr[0:3:-1] + arr[3::-1]
print(arr)