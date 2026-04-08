arr = [1,2,4]

ans = []


def subsetSum(i, total):
    if i == len(arr):
        ans.append(total)
        return

    subsetSum(i+1, total + arr[i])
    subsetSum(i+1, total)


subsetSum(0, 0)

print(ans)