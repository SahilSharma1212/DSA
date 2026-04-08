arr = [11,15,20,1,4,5,6,8,9,10]

left = 0
right = len(arr) - 1
target = 20

isfound = False

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        isfound = True
        print(arr[mid])
        break

    # left half sorted
    if arr[left] <= arr[mid]:
        if arr[left] <= target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    # right half sorted
    else:
        if arr[mid] < target <= arr[right]:
            left = mid + 1
        else:
            right = mid - 1

if not isfound:
    print("not found")