# ------------------------------------------------------
#---------------BRUTE FORCE-----------------------------
# ------------------------------------------------------


# arr = [1,0,-1,0,-2,2]
# ans = set()
# n =len(arr)
# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             for m in range(k + 1, n):
#                 if arr[i] + arr[j] + arr[k] + arr[m] == 0:
#                     quad = [arr[i], arr[j], arr[k], arr[m]]
#                     quad.sort()
#                     ans.add(tuple(quad))


# print(ans)







# ------------------------------------------------------
#---------------TWO POINTER-----------------------------
# ------------------------------------------------------


arr = [1,0,-1,0,-2,2]
arr.sort()
ans = []
n =len(arr)

for i in range(n-3):
    if i > 0 and arr[i] == arr[i-1]:
        continue

    for j in range(i+1, n-2):
        if i > 0 and arr[j] == arr[j-1]:
            continue

        left = j+1
        right = n-1

        while left < right:

            total = arr[i] + arr[j] + arr[left] + arr[right]

            if total == 0:
                ans.append([arr[i], arr[j], arr[left], arr[right]])

                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while right > left and arr[right] == arr[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -=1

print(ans)