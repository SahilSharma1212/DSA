arr = [
 [5, 1, 9, 0],
 [2, 3, 4, 8],
 [0, 6, 7, 1],
 [3, 2, 1, 5]
]

isFirstRowZero = False
isFirstColZero = False

# checking first col
for i in range(len(arr)):
    if arr[i][0] == 0:
        isFirstColZero = True
        break
# checking first row
for i in range(len(arr[0])):
    if arr[0][i] == 0:
        isFirstRowZero = True
        break

# passing and updating 0
for i in range(1, len(arr)):
    for j in range(1,len(arr[0])):
        if arr[i][j] == 0:
            arr[0][j] = 0
            arr[i][0] = 0

# setting col zeros
for i in range(len(arr[0])):
    if arr[0][i] == 0:
        for j in range(1,len(arr)):
            arr[j][i] = 0

# setting row zeros
for i in range(len(arr)):
    if arr[i][0] == 0:
        for j in range(1,len(arr[0])):
            arr[i][j] = 0

# if firstrow 0 
if isFirstColZero:
    for i in range(len(arr)):
        arr[0][i] = 0


# if firstrow 0 
if isFirstRowZero:
    for i in range(len(arr[0])):
        arr[i][0] = 0

for a in arr:
    print(a)