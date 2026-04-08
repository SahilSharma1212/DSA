arr = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]

posArr = []
negArr = []

for i in arr:
    if i >= 0:
        posArr.append(i)
    else:
        negArr.append(i)
arr.clear()
while len(posArr) > 0 and len(negArr) > 0:
    arr.append(posArr.pop())
    arr.append(negArr.pop())

while len(posArr) > 0:
    arr.append(posArr.pop())


while len(negArr) > 0:
    arr.append(negArr.pop())


print(arr)