arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

left = 0
right = len(arr[0]) - 1
top = 0
bottom = len(arr) - 1

a = []

while left <= right and top <= bottom:

    # left → right
    for i in range(left, right + 1):
        a.append(arr[top][i])
    top += 1

    # top → bottom
    for i in range(top, bottom + 1):
        a.append(arr[i][right])
    right -= 1

    # right → left
    if top <= bottom:
        for i in range(right, left - 1, -1):
            a.append(arr[bottom][i])
        bottom -= 1

    # bottom → top
    if left <= right:
        for i in range(bottom, top - 1, -1):
            a.append(arr[i][left])
        left += 1

print(a)