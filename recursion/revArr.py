arr = [1,2,3,4,5,6,7,8]



def rev(arr, n):
    if n >= len(arr)//2:
        return arr
    else:
        arr[n], arr[len(arr)-1-n] = arr[len(arr)-1-n], arr[n]
        return rev(arr, n+1)
    


print(rev(arr,0))