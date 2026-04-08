import sys

# -----------------------------------------
# LARGEST
# -----------------------------------------

arr = [2,4,56,7,4,2,21,154,6]
print(max(arr))



# -----------------------------------------
# SECOND LARGEST
# -----------------------------------------
lar = max(arr[0], arr[1])
sec = min(arr[0], arr[1])
for i in range(2, len(arr)):
    if arr[i] > lar:
        sec = lar
        lar = arr[i]
    elif arr[i] < lar and arr[i] > sec:
        sec = arr[i]

print(f"Second Largest: ", sec)




# -----------------------------------------
# SORTED ARRAY
# -----------------------------------------

arr.sort()
print(f"Sorted Array: ", arr)

intervals = [[2,1], [1,3]]
intervals.sort()
print(f"Sorted Intervals: ", intervals)

arr2 = sorted(intervals)
print(arr2)