arr = [3,4,4,4,8,9,9,10,12,12,14,15]

n = len(arr)
left = 0
right = len(arr)-1
tar = 20
floor, ceil = -1, -1

while left < n and right >= 0 and left <= right:

    mid = (left + right)//2

    if arr[mid] == tar:
        floor, ceil = tar, tar
        break
    elif arr[mid] > tar:
        ceil = arr[mid]
        right = mid-1
    else:
        floor = arr[mid]
        left = mid+1

print(f"{floor}, {ceil}")