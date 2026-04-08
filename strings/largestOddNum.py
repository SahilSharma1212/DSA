num = "67895326"
idx = len(num)-1
for i in range(len(num)-1, 0, -1):
    if int(num[i]) % 2 != 0:
        idx = i
        break

print(idx)

print(f"num is - {int(num[:idx+1])}")