# ------------------------------------------------------
#---------------BRUTE FORCE-----------------------------
# ------------------------------------------------------


arr = [1,0,-1,0,-2,2]
ans = set()

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            for m in range(k+1, len(arr)):
                if arr[i] + arr[j] + arr[k] + arr[m] == 0:
                    a = [arr[i], arr[j], arr[k], arr[m]]
                    a.sort()
                    a = tuple(a)
                    ans.add(a)


print(ans)