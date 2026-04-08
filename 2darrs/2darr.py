arr = [[1,2,3], [4,5,6]]

rows = len(arr)
col = len(arr[0])

i = 0
while i < rows:
    j = 0
    while j < col:
        print(arr[i][j], end=" ")   # stay on same line
        j += 1
    print()   # move to next line after each row
    i += 1