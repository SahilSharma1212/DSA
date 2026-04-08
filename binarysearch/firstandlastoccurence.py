arr = [1,2,3,3,3,3,3,5,6,8,9,9,10]

tar = 7

left = 0
right = len(arr)-1

isfound = False

while left <= right:

    mid = (left + right)//2

    if arr[mid] == tar:
        isfound = True
        left , right = mid, mid
        
        while arr[left-1] == arr[left]:
            left -= 1
        while arr[right+1] == arr[right]:
            right += 1
        break
    elif arr[mid] > tar:
        right = mid - 1
    else:
        left = mid + 1

if isfound:
    print(f"{left}, {right}")
else:
    print("-1, -1")