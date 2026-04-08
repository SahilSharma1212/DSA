arr = ["flow", "flight", "flower"]

arr.sort()
print(arr)

i = 0
ans = ""
first = arr[0]
last = arr[len(arr)-1]

print(first,last)

while first[i] == last[i]:
    i += 1

print(f"ans is : {first[:i]}")