# ------------------------------------------------------
#---------------BRUTE FORCE-----------------------------
# ------------------------------------------------------


# arr = [-1,0,1,2,-1,-4]
# ans = set()

# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         for k in range(j, len(arr)):
#             if arr[i] + arr[j] + arr[k] == 0:
#                 a = [arr[i], arr[j], arr[k]]
#                 a.sort()
#                 a = tuple(a)
#                 ans.add(a)


# print(ans)





# ------------------------------------------------------
#---------------TWO POINTER-----------------------------
# ------------------------------------------------------

arr = [-1,0,1,2,-1,-4]

arr.sort()

n = len(arr)
ans = []
for i in range(n):

    if i > 0 and arr[i] == arr[i-1]:
        continue

    low = i+1
    high = n-1

    while low < high:
        
        total = arr[i] + arr[low] + arr[high]

        if total == 0:
            ans.append([arr[i], arr[low], arr[high]])

            while low < high and arr[low] == arr[low+1]:
                low += 1
            while high > low and arr[high] == arr[high-1]:
                high -= 1
            
            low += 1
            high -= 1
        elif total < 0:
            low +=1
        else:
            high -=1


print(ans)